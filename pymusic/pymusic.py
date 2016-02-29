#!/usr/bin/env python

import curses

screen = curses.initscr()

screen.addstr(0, 2, "Welp, what'll this do?")
screen.refresh()
screen.getch()

curses.endwin()
