import os
from pygame import *
import block
import monsters

MOVE_SPEED = 7
MAVE_EXTRA_SPEED = 2.5
WIDTH, HEIGHT, COLOR = 22, 32, '#888888'
JUMP_POWER, JUMP_EXTRA_POWER, GRAVITY = 10, 1, 0.25
ANIMATION_DELAY, ANIMATION_SUPER_SPEED_DELAY = 0.1, 0.05

ICON_DIR = os.path.dirname(__file__)
ANIMATION_RIGHT = [ICON_DIR]
ANIMATION_LEFT = [ICON_DIR]
ANIMATION_JUMP = [ICON_DIR]
ANIMATION_JUMP_RIGHT = [ICON_DIR]
ANIMATION_JUMP_LEFT = [ICON_DIR]
ANIMATION_STAY = [ICON_DIR]

class Player(sprite.Sprite):
    def __init__(self):
        # sprite.Sprite.__init__(self)
        super().__init__(self)
        pass

    def update(self, left, right, up, running, platform):
        if up:
            pass
        if left:
            pass
        if right:
            pass

    def colllide(self, x_val, y_val, platforms):
        pass

    def teleporting(self, go_x, go_y):
        self.rect.x = go_x
        self.rect.y = go_y

    def die(self):
        time.wait(500)
        self.teleporting(self.start_x, start_y)
