from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def random_hand_arrow():
    h_x = random.randrange(0, 800)
    h_y = random.randrange(0, 600)
    print(h_x, h_y)

def move_with_hand_arrow():

    pass


running = True

while running:
    random_hand_arrow()
    #move_with_hand_arrow()
    handle_events()

