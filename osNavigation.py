#!/bin/python
# Navigating the file system and interating over files
#ref: https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

import glob, os
for file in glob.glob("*"):
    print(file) # print file in current directory

# os.chdir('/home/enumtheworld/pillow') change current working directory
# os.getcwd() gets current working directory
