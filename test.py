from commands import Command
class Butt(Command):
    def __init__(self):
        self.butt = 'butt'

butt = Butt()
print isinstance(butt, Command)