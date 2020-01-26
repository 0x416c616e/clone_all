#!/usr/bin/env python3
#Alan's Simple IO module (ASIO)

#The purpose of this module is to make IO simpler.
#You can open a file with a single function call.
#You can write data to a file with a single function call.
#You can open and load data from a file with a single function call.
#You can download a file with a single function call.
#You can download a file and write it to disk with a single function call.


import sys
import requests
import io
import os
import shutil


#=====Exception message=====
#used for many functions in this module
def ex_exit(e):
    print(e)
    print(e.args)
    sys.exit(1)

def ex_msg(filename, e, e_str, operation):
    msg = "(" + e_str + ") IO exception when " + operation
    msg += " " + filename + ":"
    print(msg)
    ex_exit(e)



#=====Deletion functions=====

#delete a file that exists
def delete(filename):
    try:
        os.remove(filename)
    except IOError as e:
        ex_msg(filename, e, "delete", "deleting")

#delete file, then make new blank file with the same filename
def clear_file(filename):
    try:
        f = open(filename, "w")
        f.write("")
        f.close()
    except IOError as e:
        ex_msg(filename, e, "clear_file", "deleting")

#confirmation
#exampe usage: confirm("example.txt", "delete")
def confirm(operation, filename):
    question = "Are you sure you want to "
    question += + operation + " " + filename + "? y/n: "
    choice = input(question)
    if ((choice.lower() == "n") or (choice.lower() == "no")):
        #user does not want to proceed with IO operation
        return False

#ask a user before deleting something
def confirm_delete(filename):
    if (confirm("delete", filename)):
        delete(filename)

#delete all files in a given directory
#but does not delete the folder itself
def clear_directory(folder):
    for filename in os.listdir(folder):
        delete(filename)

#delete an entire directory
def delete_directory(folder):
    try:
        shutil.rmtree(folder)
    except IOError as e:
        ex_msg(folder, e, "delete_directory", "deleting")


#=====Check functions=====
#check if file exists
def exists(filename):
    return os.path.exists(filename)

def does_not_exist(filename):
    return (not os.path.exists(filename))

#check if a file exists, and then delete it if it does
def delete_if_exists(filename):
    if (exists(filename)):
        delete(filename)



#=====Write functions=====

#functions that start in "write" are OVERWRITE functions

#function for safely downloading utf8 text data
#won't work for binary files i.e. jpeg or exe
#usage example: safe_write_text("something.html", response.text)
def write_utf8(filename, data):
    try:
        write_file = io.open(filename, "w", encoding="utf-8")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        ex_msg(filename, e, "write_utf8", "writing")


#regular text file write function
#example: safe_write("results.xml", response.text)
def write_text(filename, data):
    try:
        write_file = open(filename, "w")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        ex_msg(filename, e, "write_text", "writing")

#write binary data to a file
#example: write_binary("something.jpg", response.content)
def write_binary(filename, data):
    try:
        write_file = open(filename, "wb")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        ex_msg(filename, e, "write_binary", "writing")






#=====Append functions=====
#append operations
#append mode for binary: "r+b"

#append utf8
def append_utf8(filename, append_data):
    if (exists(filename)):
        try:
            write_file = io.open(filename, "a", encoding="utf-8")
            write_file.write(append_data)
            write_file.close()
        except IOError as e:
            ex_msg(filename, e, "append_utf8", "appending")


#append text
def append_text(filename, append_data):
    if (exists(filename)):
        try:
            append_file = open(filename, "a")
            append_file.write(append_data)
            append_file.close()
        except IOError as e:
            ex_msg(filename, e, "append_text", "appending")



#append binary
def append_binary(filename, append_data):
    if (exists(filename)):
        try:
            append_file = open(filename, "r+b")
            append_file.write(append_data)
            append_file.close()
        except IOError as e:
            ex_msg(filename, e, "append_binary", "appending")

#DNE: Does Not Exist
#write if does not exist utf8

def write_dne_utf8(filename, data):
    if (does_not_exist(filename)):
        write_utf8(filename, data)

#write if does not exist text

def write_dne_text(filename, data):
    if (does_not_exist(filename)):
        write_text(filename, data)

#write if does not exist binary
def write_dne_binary(filename, data):
    if (does_not_exist(filename)):
        write_binary(filename, data)








#=====Download functions=====

#function for safely downloading a web page
#returns the response object
#if you want to write the response object to a file, do something like
#response.text
def download(dl_url):
    dl_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = ""
    try:
        response = requests.get(dl_url, dl_headers)
    except requests.RequestException as e:
        print("Request exception:")
        ex_exit(e)
    status = response.status_code
    #HTTP 200 means OK
    if (status != 200):
        print("Error code: " + str(status))
        sys.exit(1)
    elif (response == ""):
        print("Response error")
        sys.exit(1)
    else:
        #file downloaded successfully, but it's only stored in RAM,
        #not written to disk at this point
        return response

#~~~Functions that download files and then write to disk~~~

#download and save binary
def dl_write_bin(dl_url, filename):
    response = download(dl_url)
    write_binary(filename, response.content)


#download and save text
def dl_write_text(dl_url, filename):
    response = download(dl_url)
    write_text(filename, response.text)


#download and save UTF-8
def dl_write_utf8(dl_url, filename):
    response = download(dl_url)
    write_utf8(filename, response.text)




#=====Open functions=====

#open and return UTF-8

def open_utf8(filename):
    try:
        return io.open(filename, "r", encoding="utf-8")
    except IOError as e:
        ex_msg(filename, e, "open_utf8", "opening")

#open and return text
def open_text():
    print("not done")

#open and return binary
def open_binary():
    print("not done")




#=====Search functions=====

#search file for string
def search(str_to_find, filename):
    try:
        file_to_search = open(filename, "r")
        if str_to_find in file_to_search.read():
            return True
        else:
            return False
        file_to_search.close()
    except IOError as e:
        ex_msg(filename, e, "search", "searching")


#return a line that contains a search term
#from a utf-8 file
def utf8_get_line_with(str_to_find, filename):
    try:
        #open file and read line by line
        print("")
        if (exists(filename)):
            search_file = open_utf8(filename)
            line = search_file.readline()
            while line:
                if (str_to_find in line):
                    search_file.close()
                    return line
                line = search_file.readline()
            search_file.close()
            return "not_found"
    except IOError as e:
        ex_msg(filename, e, "get_line_contains", "searching")



#=====TO-DO=====


#=====Upload functions=====

#upload utf-8 file

#upload text file

#upload binary file

#post requests for the above

#ftp?
