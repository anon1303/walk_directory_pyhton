"""
Application that walks in through a given directory path

VERSION: 1
DISCRIPTION:
    This version is the first version, It is basically just a 
    basic implemtation, a straight fowrard execution
"""

import os, sys
from stat import *  
#path
path = 'D:/programming/go/'



s1 = os.path.S_ISFIFO
# s2 = os.fstat(path)
# s3 = os.lstat(path)


print(s1)
# print(s2)
# print(s3)



print("\n")
mypath = os.scandir(path)

print("Files and Directories in '% s':" % path)
for entry in mypath:
    if entry.is_file():
        print("FILES: ",entry.name)
    if entry.is_dir():
        print(entry.name)
        folder = entry.name
        subpath = os.scandir(path+folder)
        for entry in subpath:
            print(" --> ",entry.name)


        # print(entry.name)
