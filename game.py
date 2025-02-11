import os.path
import pygame
from pygame import Color

FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#000000"
FILE_DIR = os.path.dirname(__file__)

class Game:
    def __init__(self):
        pass

    def apply(self):
        pass

    def update(self):
        pass


def camera_config(camera, target_rect):
    pass

def load_level():
    pass

def main():
    load_level()
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_mode('GG')
    bg = pygame.Surface(DISPLAY)
    bg.full(Color(BACKGROUND_COLOR))

    left = right = up = running = False

    hero = Player(player_x, player_y)

    timer = pygame.time.Clock()

    x = y = 0

    while not hero.winner:
        timer.tick(FPS)
