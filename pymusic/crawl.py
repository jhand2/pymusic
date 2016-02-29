import os
from os.path import join

def find_files(path):
    """
    Searches the file system from root to find any music files
    (mp3 by default)
    """
    for root, dirs, files in os.walk(path):
        print root

find_files("/home/")
