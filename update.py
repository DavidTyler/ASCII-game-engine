def update(active_things, screen):
    for thing in active_things:
        thing.update()
    return determine_drawable(active_things, screen)
    
def determine_drawable(active_things, screen):
    maxy, maxx = screen.getmaxyx()
    drawable = []
    for thing in active_things:
        for render in thing.renders:
            if render.y in range(0, maxy) and render.x in range(0, maxx):
                drawable.append(render)
    return drawable