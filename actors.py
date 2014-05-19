from time import time
from random import random, randint
from log import log
import curses

class Actor(object):
    def __init__(self):
        self.renders = []
    def update(self):
        pass
    def move(self, direction):
        for render in self.renders:
            if direction == "left":
                render.x -= 1
            elif direction == "right":
                render.x += 1
            elif direction == "up":
                render.y -= 1
            else:
                render.y += 1
class Ball(Actor):
    def __init__(self, x=10, y=1):
        x = randint(0, 100)
        y = randint(0, 50)
        self.renders = [Render(ord('o'), y, x)]
        self.last_moved = time()
    def oscillate(self):
        if self.renders[0].sym == ord('o'):
            self.renders[0].sym = ord('O')
        else:
            self.renders[0].sym = ord('o')
    def update(self):
        rand = random()
        if self.last_moved + random() < time():
            if rand >= 0 and rand < .25:
                direction = "left"
            elif rand >= .25 and rand < .5:
                direction = "up"
            elif rand >= .5 and rand < .75:
                direction = "right"
            else:
                direction = "down"
            self.oscillate()
            self.move(direction)
            self.last_moved = time()
class Render(object):
    def __init__(self, sym, y, x):
        self.x = x
        self.y = y
        self.sym = sym