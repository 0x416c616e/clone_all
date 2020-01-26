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
import time


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
    if (asio.search_utf8(string_404, first_page_name)):
        print("404: GitHub user " + username + " not found")
        asio.delete(first_page_name)
        sys.exit(1)
    else:
        print("User exists, proceeding...")

    #parse html and look for no repo string
    #from first_repo_page.html
    #"doesn’t have any public repositories yet."
    no_repos_string = "have any public repositories yet"
    if (asio.search_utf8(no_repos_string, first_page_name)):
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

    #program will loop until there is no "next" page,
    #at which point should_proceed will be set to False
    should_proceed = True

    #getting first 'next page'
    next_repo_string = "tab=repositories\">Next</a></div>"
    if (asio.search_utf8(next_repo_string, first_page_name)):
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
            #"next_page_url" is actually an entire line of HTML
            #the line has some undesirable stuff at the
            #beginning and end, so you need to get rid of the 
            #stuff before the next url and the stuff after it
            #and then you'll be left with just the next page url

            #strip front off line using find() and string slicing
            #https://www.programiz.com/python-programming/methods/string/find
            start_index = next_page_url.find("https://")
            #get rid of beginning of line, starting only with https:// now
            next_page_url = next_page_url[start_index:]
            #finding where the url ends
            trailing_data = "s\">Next</a></div>"
            end_index = next_page_url.find(trailing_data)
            #add one to avoid an off-by-one error
            end_index = end_index + 1
            #get rid of stuff at the end after the URL is finished
            next_page_url = next_page_url[:end_index]
            print("Next page URL for page 2:" + next_page_url)

            #loop for finding pages 2+
            while (should_proceed == True):
                #the previous loop's "next" is this loop's "current"
                current_repo_page_url = next_page_url
                #repo_page_2.html, repo_page_3.html, repo_page_4.html, etc
                page_name = "html/repo_page_" + str(number_of_pages) + ".html"
                print("page name: " + page_name)
                print("current repo page url:" + current_repo_page_url)
                #I got a 429 Too Many Requests error until I added this sleep()
                time.sleep(2)
                asio.dl_write_utf8(current_repo_page_url, page_name)
                #if there is yet another page
                if (asio.search_utf8(next_repo_string, page_name)):
                    print("another page was found")
                    next_page_url = ""
                    next_page_url = asio.utf8_get_line_with(next_repo_string, page_name)
                    if (next_page_url == ""):
                        print("error")
                        sys.exit(1)
                    elif (next_page_url == "not_found"):
                        print("there is no next page")
                        should_proceed = False
                    else:
                        print("there is another page")
                        number_of_pages += 1
                        #at this point, next_page_url is really a line that contains too much stuff, with some
                        #stuff at the beginning and end that needs to be removed

                        #==========================================================
                        #the commented out block was replaced by the 
                        #convert this block (separated by spaces) to function in asio.py

                        ##rfind means find the LAST occurrence
                        #prefix_data = "https://"
                        #start_index = next_page_url.rfind(prefix_data)
                        ##get rid of beginning of line, starting only with https:// now
                        #next_page_url = next_page_url[start_index:]
                        ##finding where the url ends
                        #trailing_data = "s\">Next</a></div>"
                        #end_index = next_page_url.find(trailing_data)
                        ##add one to avoid an off-by-one error
                        #end_index = end_index + 1
                        ##get rid of stuff at the end after the URL is finished
                        #next_page_url = next_page_url[:end_index]
                        #==========================================================
                        next_page_url = asio.get_last_string_from_line_utf8("https://", "s\">Next</a></div>", next_page_url)


                        print("Next page URL for page " + str(number_of_pages) + ": " + next_page_url)
                
                #no more pages     
                else:
                    print("No more pages to find and download.")
                    should_proceed = False
            

        #================================================
        #make the above stuff generalizable and able to loop and whatnot
        #to download and search through as many html pages as possible
        


    else:
        print("User only has one page of repos.")    


    #getting here is when you've finished downloading all the html pages
    #that are just lists of repos
    #and now you need to get all the individual repo links out of them
    #if a repo link is this: https://github.com/0x416c616e/clone_all
    #then its clone link is this: https://github.com/0x416c616e/clone_all.git
    #just append ".git"

    print("Number of pages: " + str(number_of_pages))



#boilerplate
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()