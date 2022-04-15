"""
Application that walks in through a given directory path

VERSION: 2
DISCRIPTION:
    This version is the second version, from the first version this one
    uses recursion and functions
"""

import os, sys


def get_path_stat(path):
    status = os.stat(path)
    print("*"*10 + "PATH STAT" + "*"*10)
    print(status)
    print("\n")
    

def get_list(path):

    files = os.scandir(path)
    # all_files = list()

    for file in files:

        if file.is_file():
            print("- ",file.name)
        
        fullPath = os.path.join(path, file)
        if os.path.isdir(fullPath):
            print(file.name)
            # folder = entry.name
            subpath = get_list(fullPath)

def main():

    path = 'D:/programming/go/'


    get_path_stat(path)
    get_list(path)


if __name__ == '__main__':
    main()