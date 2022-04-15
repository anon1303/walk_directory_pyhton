"""
Application that walks in through a given directory path

VERSION: 3
DISCRIPTION:
    This version is the second version, from the second version this one
    uses recursion, functions and added command-line parsing library(Docopt)
"""

import os, sys
from docopt import docopt
from stat import *



def get_path():
    """Function to get command line arguments.

    Defines arguments needed to run this program.

    :return: Dictionary with arguments
    :rtype: dict
    """
    
    usage = """
    Usage:
        walkv3.py <PATHNAME> -c
        walkv3.py -h | --help

    Options:
        -h --help            Show this message and exit
        -s <PATHNAME>        Directory full path

    """

    args = docopt(usage)
    return args 


def get_path_stat(path):

    print("*"*10 + "PATH STAT" + "*"*10)
    print("SOCK ---> ",S_IFSOCK)
    print("LINK ---> ",S_IFLNK)
    print("REG ---> ",S_IFREG)
    print("BLK ---> ",S_IFBLK)
    print("DIR ---> ",S_IFDIR)
    print("CHR ---> ",S_IFCHR)
    print("FIFO ---> ",S_IFIFO)
    print("DOOR ---> ",S_IFDOOR)

    print("\n")
    # [ REG  => S_IFREG  ],
    # [ DIR  => S_IFDIR  ],
    # [ LNK  => S_IFLNK  ],
    # [ SOCK => S_IFSOCK ],
    # [ BLK  => S_IFBLK  ],
    # [ CHR  => S_IFCHR  ],
    # [ FIFO => S_IFIFO  ]

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode




        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):

            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    # print('visiting', file)
    pass


def get_list(path):

    files = os.scandir(path)
    # all_files = list()

    for file in files:

        if file.is_file():
            print("File: ",file.name)
        
        fullPath = os.path.join(path, file)
        if os.path.isdir(fullPath):
            print("Dir: ",file.name)
            # folder = entry.name
            subpath = get_list(fullPath)

def main(PATH):

    path = PATH['<PATHNAME>']


    get_path_stat(path)
    get_list(path)


if __name__ == '__main__':
   

    try:
        PATH = get_path()
        walktree(PATH['<PATHNAME>'], visitfile)
        main(PATH)
        
    except OSError:
        print("\nPath or directory name syntax is incorrect: ",PATH['<PATHNAME>'])
    else:
        pass