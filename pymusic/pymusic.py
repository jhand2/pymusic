#!/usr/bin/env python

import curses
from curses import wrapper
import threading

# Local imports
import loader
import player


class MusicUI(object):
    """
    A music player UI object. Handles all UI input and display.
    """

    def __init__(self, screen):
        """
        Initializes member variables for MusicUI
        """
        self.scr = screen
        self.pad = None
        self.pad_pos = None
        self.curs_pos = None
        self.max_x = None
        self.max_y = None
        self.song_thread = None
        self.music = player.Player()

    def draw_ui(self, songs, refresh_only):
        """Draws the UI. Basically called every time any interaction happens

        args:
            songs -- list of currently playable song objects
            refresh_only -- boolean, if True only refreshes the screen
                                     if False inits screen and refreshes
        """
        self.max_y, self.max_x = self.scr.getmaxyx()
        if not refresh_only:
            self.scr.addstr(0, 0, "PYMusic Music Player")

            self.pad = curses.newpad(self.max_y, self.max_x)
            index = 0
            self.pad_pos = 1
            self.curs_pos = self.pad_pos

            for s in songs:
                index += 1
                self.pad.addstr(index, 2, s.name)
            curses.curs_set(1)
            self.scr.refresh()

        self.pad.refresh(self.pad_pos, 0, 1, 0, self.max_y, self.max_x - 1)
        curses.setsyx(self.curs_pos, 2)
        curses.doupdate()

    def get_input(self, songs):
        """
        Gets input from the user
        """
        while True:
            ch = self.scr.getch()
            if ch == curses.KEY_DOWN or ch == ord('j'):
                if (self.curs_pos < self.max_y - 1 and
                        self.curs_pos < len(songs)):
                    self.curs_pos += 1
                    # self.pad_pos += 1
            elif ch == curses.KEY_UP or ch == ord('k'):
                if self.curs_pos > self.pad.getbegyx()[0]:
                    self.curs_pos -= 1
                    # self.pad_pos -= 1
            elif ch == curses.KEY_ENTER or ch == 10 or ch == 13:
                song_index = self.curs_pos - self.pad_pos
                if not self.play_song(songs[song_index]):
                    break
            elif ch == ord('q'):
                # if self.song_thread is not None:
                self.music.stop()

                break
            self.draw_ui(songs, True)

    def play_song(self, s):
        """
        Plays song s in the background

        args:
            s -- song to be played
        """
        try:
            self.music.stop()
            self.song_thread = threading.Thread(target=self.music.play,
                                                args=(s, ))
            self.song_thread.start()
            return True
        except:
            return False


class App(object):
    def __init__(self, screen):
        """
        Initializes the pymusic application
        """
        self.screen = screen

        """Crawls current user's Music Directory and loads all playable
        music files"""
        songs = loader.find_files("/home/jordan/Music")
        ui = MusicUI(screen)
        ui.draw_ui(songs, False)
        ui.get_input(songs)


if __name__ == "__main__":
    wrapper(App)
