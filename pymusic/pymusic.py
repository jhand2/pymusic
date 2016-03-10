#!/usr/bin/env python

import curses
from curses import wrapper

# Local imports
import crawl


class MusicUI(object):

    def __init__(self, screen):
        self.scr = screen
        self.pad = None
        self.pad_pos = None
        self.curs_pos = None

    def draw_ui(self, songs, refresh_only):
        if not refresh_only:
            self.scr.addstr(0, 0, "PYMusic Music Player")

            self.pad = curses.newpad(100, 100)
            index = 0
            self.pad_pos = 1

            for s in songs:
                # if index == self.pad_pos:
                    # mode = curses.A_REVERSE
                # else:
                    # mode = curses.A_NORMAL
                index += 1
                self.pad.addstr(index, 2, s.name)
            curses.curs_set(1)

        max_x = self.scr.getmaxyx()
        self.scr.refresh()
        self.pad.refresh(self.pad_pos, 0, 1, 0, len(songs), max_x[1] - 1)
        curses.setsyx(1, 1)
        curses.doupdate()

    def get_input(self, songs):
        while True:
            ch = self.scr.getch()
            if ch == curses.KEY_DOWN or ch == ord('j'):
                if self.pad_pos < len(songs):
                    self.pad_pos += 1
            elif ch == curses.KEY_UP or ch == ord('k'):
                if self.pad_pos > 0:
                    self.pad_pos -= 1
            elif ch == ord('q'):
                break
            self.draw_ui(songs, True)


class App(object):
    def __init__(self, screen):
        self.screen = screen

        songs = crawl.find_files("/home/jordan/Music")
        ui = MusicUI(screen)
        ui.draw_ui(songs, False)
        ui.get_input(songs)


if __name__ == "__main__":
    wrapper(App)
