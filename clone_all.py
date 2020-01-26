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
    
    first_page_name = "html/repo_page_1.html"

    print("Downloading with new modularized IO code")
    #download the first repo page and save it as first_repo_page.html
    asio.dl_write_utf8(first_repo_page_url, first_page_name)

    #search for 404 string: user might not even exist, after all
    string_404 = '<img alt="404 &ldquo;This is not the web page you are looking for&rdquo;'
    if (asio.search(string_404, first_page_name)):
        print("404: GitHub user " + username + " not found")
        asio.delete(first_page_name)
        sys.exit(1)
    else:
        print("User exists, proceeding...")

    #parse html and look for no repo string
    #from first_repo_page.html
    #"doesn’t have any public repositories yet."
    no_repos_string = "have any public repositories yet"
    if (asio.search(no_repos_string, first_page_name)):
        print("User has no repos")
        #can't proceed with program if the user has no repos
        asio.delete(first_page_name)
        sys.exit(1)
    else:
        print("User apparently has repos")
    
    #proceed with program
    #at this point, it's not a 404, and the user has repos

    #see if there is more than one page of repos
    #if there's more than one page, you will find this string in first_page_name:
    #tab=repositories">Next</a></div>

    #number of html pages of repos
    number_of_pages = 1

    #will loop until there is no "next" page,
    #at which point should_proceed will be set to False
    should_proceed = True

    next_repo_string = "tab=repositories\">Next</a></div>"
    if (asio.search(next_repo_string, first_page_name)):
        print("User has more than one page worth of repos")
        number_of_pages += 1
        #================================================
        #test getting the single next page, then later put it in a while loop
        #using should_proceed as the exit condition
        next_page_url = ""
        next_page_url = asio.utf8_get_line_with(next_repo_string, first_page_name)
        if (next_page_url == ""):
            print("error")
            sys.exit(1)
        elif (next_page_url == "not_found"):
            print("there is no next page")
            should_proceed = False
        else:
            print("Next page URL: " + next_page_url)
        #================================================
        #make the above stuff generalizable and able to loop and whatnot
        #to download and search through as many html pages as possible
        


    else:
        print("user only has one page of repos")    


    #getting here is when you've finished downloading all the html pages
    #that are just lists of repos
    #and now you need to get all the individual repo links out of them
    #if a repo link is this: https://github.com/0x416c616e/clone_all
    #then its clone link is this: https://github.com/0x416c616e/clone_all.git
    #just append ".git"

    




#boilerplate
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()