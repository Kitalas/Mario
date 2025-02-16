import os
from pygame import *
import block
import monsters
from settings import MOVE_SPEED, MAVE_EXTRA_SPEED, WIDTH, HEIGHT, COLOR, JUMP_POWER, JUMP_EXTRA_POWER, GRAVITY, ANIMATION_DELAY, ANIMATION_SUPER_SPEED_DELAY, ICON_DIR_PLAYER, ANIMATION_RIGHT, ANIMATION_LEFT, ANIMATION_JUMP, ANIMATION_JUMP_RIGHT, ANIMATION_JUMP_LEFT, ANIMATION_STAY


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
