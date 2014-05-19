from time import time
def log(log_item):
    f = open('log.txt', 'a')
    f.write('{}: {}\n'.format(time(), log_item))
    f.close()