import termios, fcntl, sys, os
from threading import Thread
from commands import Command
from log import log
import curses

class InputHandler(Thread):
    def __init__(self, screen):
        Thread.__init__(self)
        self.screen = screen
    def run(self):
        try:
            while True:
                c = self.screen.getkey()
                log(c)
        except Exception as e:
            log(e)