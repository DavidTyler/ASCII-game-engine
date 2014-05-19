import curses
from sys import exit

class Renderer(object):
    def __init__(self):
        self.screen = curses.initscr()
        self.maxy, self.maxx = self.screen.getmaxyx()
        # self.screen.nodelay(1)
        curses.curs_set(0)
        curses.noecho()
    def render(self, drawable):
        self.screen.clear()
        for render in drawable:
            try:
                self.screen.addch(render.y, render.x, render.sym)
            except curses.error:
                exit()
        self.screen.refresh()
    def destroy(self):
        curses.endwin()