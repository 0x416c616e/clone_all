# Design doc for how this app will work

0. A user can have zero, one, or many repos. A user might have less than one full page of repos, one full page, more than one but not full, or multiple full pages of repos. As such, you need to consider all of them as possibilities.
1. Get username from the user as a command line arg
2. Build a URL, such as the following:
	- https://github.com/0x416c616e?tab=repositories
3. Use requests to download the file in a subfolder, called html/
4. Parse the HTML file and look for this (without quotes):
	-"doesn’t have any public repositories yet."
5. If the above string is in the page, then exit the program because they don't have any repos.  
6. Parse the HTML file and look for this:
	-"&amp;tab=repositories">Next</a></div>"
7. If the above string is within the document, then you can proceed with getting the next page. Stub: print "there is a next page"
8. To-do: how to loop and download multiple files by finding the url of the "next" button's link
9. To-do: If there are next pages, download them all and loop. 
10. To-do: Look through all the HTML files again, but this time to find repo download links.
11. To-do: create a reset.sh script to delete downloaded files. Optional/not required for this to work.
12. To-do: Use the GitHub repo links to clone all the repos to the repos/ subdirectory.
13. To-do: used linked list for the page links, use stack for the links of repos to clone



