import os
from os.path import join
from song import Song

def find_files(path):
    """
    Searches the file system from root to find any music files
    (mp3 by default)
    """
    songs = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".mp3"):
                s = Song(f, "Artist", root + f)
                songs.append(s)
    return songs
