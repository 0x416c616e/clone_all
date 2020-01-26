#!/usr/bin/env python3
#Alan's Simple IO

import sys
import requests
import io

#function for safely downloading utf8 text data
#won't work for binary files i.e. jpeg or exe
#usage example: safe_write_text("something.html", response.text)
def write_utf8(filename, data):
    try:
        write_file = io.open(filename, "w", encoding="utf-8")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        print("(UTF-8) IO exception when writing to " + filename + ":")
        print(e.args)
        sys.exit(1)


#regular text file write function
#example: safe_write("results.xml", response.text)
def write_text(filename, data):
    try:
        write_file = open(filename, "w")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        print("(Text) IO exception when writing to " + filename + ":")
        print(e.args)
        sys.exit(1)

#write binary data to a file
def write_binary(filename, data):
    try:
        write_file = open(filename, "wb")
        write_file.write(data)
        write_file.close()
    except IOError as e:
        print("(Binary) IO exception when writing to " + filename + ":")
        print(e.args)
        sys.exit(1)


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
        print(e.args)
        sys.exit(1)
    status = response.status_code
    #HTTP 200 means OK
    if (status != 200):
        print("Error code: " + status)
        sys.exit(1)
    elif (response == ""):
        print("Response error")
        sys.exit(1)
    else:
        #file downloaded successfully, but it's only stored in RAM,
        #not written to disk at this point
        return response

    