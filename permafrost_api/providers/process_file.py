#
# Process a test file
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

import sys

def main():
    arguments = len(sys.argv) - 1
    if arguments != 1:
        print("Provide the file name as command line parameter.")
        return

    f = open(sys.argv[1], "a")
    f.write("\nWoops! I have modified the content!")
    f.close()

if __name__ == "__main__":
    main()

