import os
from pygame import *


PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_COLOR = 32, 32, '#000000'
ICON_DIR = os.path.dirname(__file__)

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        # sprite.Sprite.__init__(self)
        super().__init__(self)
        pass

class BlockDie(Platform):
    def __init__(self, x, y):
        pass

class BlockTeleport(Platform):
    def __init__(self, x, y):
        pass

    def update(self):
        pass

class Princess(Platform):
    def __init__(self, x, y):
        pass

    def update(self):
        pass