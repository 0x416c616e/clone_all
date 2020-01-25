#!/usr/bin/env python3
#Clone All
#Clone all repos from a specific user on GitHub

import sys

def main():
    if (len(sys.argv) != 2):
        print("Error with number of command line args.")
        print("Here's how you use this program:")
        print("clone_all.py username_goes_here")
        sys.exit(1)
    else:
        print("Correct number of command line args.")
        username = sys.argv[1]
        print("Username: " + username)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()