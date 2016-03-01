#!/usr/bin/env python

import curses
from curses import wrapper

# Local imports
import crawl


def main(scr):
    """Does curses stuffs"""

    scr.addstr(0, 0, "PYMusic Music Player")
    songs = crawl.find_files("/home/jordan/Music")
    index = 2
    for s in songs:
        scr.addstr(index, 0, s.name)
        index += 1

    scr.refresh()
    scr.getch()


wrapper(main)
