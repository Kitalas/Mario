import pygame
import time

PLAYING, PAUSED, STOPPED = 'playing', 'paused', 'stopped'

NORTH, SOUTH, WEST, EAST = 'north', 'south', 'west', 'east'
NORTH_WEST, SOUTH_WEST, NORTH_EAST, SOUTH_EAST = 'northwest', 'southwest', 'northeast', 'southeast'

class PygAnimation:
    def __init__(self, frames, loop=True):
        pass

    def _get_start_times(self):
        pass

    def reversed(self):
        pass

    def get_copy(self):
        pass

    def get_copies(self, num_copies=1):
        pass

    def blit(self, dest_surface, dest):
        pass

    def get_frame(self, frame_num):
        pass

    def claerTransforms(self):
        pass

    def make_transform_permanent(self):
        pass

    def blit_frame_num(self):
        pass

    def play(self):
        pass

    def isFinishad(self):
        pass

