#!/usr/bin/env python3
#Clone All
#Clone all repos from a specific user on GitHub

#this program can only work as python3, not python2

#requires you to install the requests module
import sys
import requests
#io is needed to write UTF-8/Unicode instead of ASCII
import io
#Alan's Simple IO: contains 
import asio



#main program 'driver' function
def main():

    #getting command line args
    username = ""
    if (len(sys.argv) != 2):
        print("Error with number of command line args.")
        print("Here's how you use this program:")
        print("clone_all.py username_goes_here")
        sys.exit(1)
    else:
        print("Correct number of command line args.")
        username = sys.argv[1]
        print("Username: " + username)
    #proceeding with program now that cli arg has been finished


    #building URL of initial repo tab page
    #example: https://github.com/0x416c616e?tab=repositories
    first_repo_page_url = "https://github.com/" + username + "?tab=repositories"
    print("URL: " + first_repo_page_url)


    #download first repo page 
    
    first_page_name = "first_repo_page.html"

    print("Downloading with new modularized IO code")
    #download the first repo page and save it as first_repo_page.html
    asio.dl_write_utf8(first_repo_page_url, first_page_name)

    #search for 404 string: user might not even exist, after all
    string_404 = '<img alt="404 &ldquo;This is not the web page you are looking for&rdquo;'
    

    #parse html and look for no repo string
    #from first_repo_page.html
    #"doesn’t have any public repositories yet."
    no_repos_string = "have any public repositories yet"
    if (asio.search(no_repos_string, first_page_name)):
        print("User has no repos")

    else:
        print("User apparently has repos")
    




    




#boilerplate
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()