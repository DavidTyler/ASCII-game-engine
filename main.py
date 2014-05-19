from sys import exit
from time import time
from update import update
from render import Renderer
from state import State
from inputhandler import InputHandler
import actors
import threading

MS_PER_UPDATE = .015

def running(thread):
    if thread in threading.enumerate():
        return True
    else: return False

def handle_input(thread, screen):
    if thread == None or not running(thread):
        inp = InputHandler(renderer.screen)
        inp.daemon = True
        inp.start()
        return inp
        # return thread
    else: return thread

def stats(updates, input_processes, renders, total_elapsed, actor_count):
    print 'active_threads:', threading.active_count()
    print 'updates:', updates
    print 'input_processes:', input_processes
    print 'renders:', renders
    print 'time_elapsed:', total_elapsed
    print 'updates/render:', updates/float(renders)
    print 'updates/second:', updates/total_elapsed
    print 'fps:', renders/total_elapsed
    print 'actors:', actor_count

if __name__ == "__main__":
    updates = 0
    input_processes = 0
    renders = 0

    start = time()
    previous = time()
    lag = 0.0
    state = State()
    renderer = Renderer()
    t = handle_input(None, renderer.screen)
    drawable = []
    state.active_things = [actors.Ball() for x in range(100)]
    try:
        while updates < 1000:
            current = time()
            elapsed = current - previous
            previous = current
            lag += elapsed
            t = handle_input(t, renderer.screen)
            while lag >= MS_PER_UPDATE:
                drawable = update(state.active_things, renderer.screen)
                updates += 1
                lag -= MS_PER_UPDATE
            renderer.render(drawable)
            renders += 1
            total_elapsed = current-start
    except KeyboardInterrupt:
        pass
    actor_count = len(state.active_things)
    renderer.destroy()
    stats(updates, input_processes, renders, total_elapsed, actor_count)
