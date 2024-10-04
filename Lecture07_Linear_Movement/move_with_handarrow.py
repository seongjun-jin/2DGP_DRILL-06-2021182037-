from pico2d import *
import random
import math

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


x, y = 400, 300
h_x, h_y = random.randrange(0, 800), random.randrange(0, 600)
t = 0
frame = 0
speed = 0.01
head_left = False
head_right = False

def random_hand_arrow():
    global h_x, h_y, x, y, t
    h_x = random.randrange(0, 800)
    h_y = random.randrange(0, 600)
    t = 0

def move_with_hand_arrow():
    global x, y, t, head_left, head_right
    if t >= 1:
        random_hand_arrow()

    t += speed
    x_prev, y_prev = x, y
    x = (1 - t) * x + t * h_x
    y = (1 - t) * y + t * h_y

    if(x_prev > x):
        head_left = True
        head_right = False
    if(x_prev < x):
        head_right = True
        head_left = False


running = True

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    hand_arrow.draw(h_x, h_y)
    if head_right:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    if head_left:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    move_with_hand_arrow()

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)
