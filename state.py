class State(object):
    def __init__(self, active_things=[]):
        self.active_things = active_things
    def update(self):
        for thing in self.active_things:
            thing.update()