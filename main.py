import time
import curses
from random import randint

WINDOW_HEIGHT = 20
WINDOW_WIDTH = 60

y = WINDOW_HEIGHT
x = WINDOW_WIDTH

curses.initscr()
curses.noecho()
curses.curs_set(0)

win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
win.border(0)
win.nodelay(1)

curses.endwin()

p1 = [(8, 5), (9, 5), (10, 5)]
p2 = [(8, 55), (9, 55), (10, 55)]

ESC = 27
key = curses.KEY_RIGHT
while key != ESC:

    event = win.getch()

    for c in p1:
        win.addch(c[0], c[1], 'H')

    for ac in p2:
        win.addch(ac[0], ac[1], 'H')


curses.endwin()
