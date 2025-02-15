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
