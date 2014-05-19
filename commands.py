from log import log
from time import time

class Command(object):
    def __init__(self):
        pass
    def execute(self, actor):
        pass
    def receive_input(self, inp):
        pass

class MoveCommand(Command):
    def __init__(self, direction):
        this.direction = direction
    def execute(self, actor):
        actor.move(direction)

class CommandStream(object):
    def __init__(self, commands=[], path='command_log.txt'):
        self.commands = commands
        self.executed_commands = []
        self.path = path
    def add(self, command):
        if isinstance(command, Command):
            self.commands.append(command)
        else:
            log('Attempted insertion of {} into command stream'.format(command))
    def pop(self, actor):
        if len(self.commands) > 0:
            command = self.commands.pop(0)
            if isinstance(command, Command):
                command.execute(actor)
                self.executed_commands.append((time(), command))
            else:
                log('Attempted execution of {} as a command'.format(command))
    def log_executed(self):
        with open(self.path, 'a') as f:
            [f.write('{}\n'.format(command)) for command in self.executed_commands]
            self.executed_commands = []
class CommandInterpreter(object):
    def __init__(self, path='controls.txt'):
        with open(self.path, 'r') as f:
            try:
                self.controls = []
                for line in self.path:
                    pass
            except:
                pass