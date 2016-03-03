#!/usr/bin/env python

import curses
from curses import wrapper

# Local imports
import crawl


class MusicUI(object):

    def __init__(self, screen):
        self.scr = screen

    def refresh(self, nrows, xmax):
        self.scr.refresh()
        self.pad.refresh(pad_pos, 0, 1, 0, nrows, xmax - 1)

    def init_ui(self, songs, refresh_only):

        self.scr.addstr(0, 0, "PYMusic Music Player")

        self.pad = curses.newpad(100, 100)
        index = 1
        self.pad_pos = 1

        for s in songs:
            if index == pad_pos:
                mode = curses.A_REVERSE
            else:
                mode = curses.A_NORMAL
                pad.addstr(index, 2, s.name, mode)
                index += 1
        max_x = self.scr.getmaxyx()
        curses.curs_set(1)
        curses.curs_set(0)
        refresh(len(songs), max_x, pad)

    def add_pad()

    def get_input(songs):
        while True:
            ch = scr.getch()
            if ch == curses.KEY_DOWN:
                if pad_pos < len(songs):
                    pad_pos += 1
            elif ch == curses.KEY_UP:
                if pad_pos > 0:
                    pad_pos -= 1
            elif ch == ord('q'):
                break
            refresh(len(songs))


class App(object):
    def __init__(self, screen):
        self.screen = screen

        songs = crawl.find_files("/home/jordan/Music")
        ui = MusicUI(screen)
        draw_ui(songs)
        get_input(songs)


if __name__ == "__main__":
    wrapper(App)
