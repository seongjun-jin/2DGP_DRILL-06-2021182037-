from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def random_hand_arrow():
    h_x = random.randrange(0, 800)
    h_y = random.randrange(0, 600)
    print(h_x, h_y)

def move_with_hand_arrow():

    pass

while(True):
    random_hand_arrow()
    move_with_hand_arrow()

