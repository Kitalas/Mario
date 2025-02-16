import os
import pygame
from pygame import Color
from settings import WIN_WIDTH, WIN_HEIGHT, DISPLAY, BACKGROUND_COLOR, FPS, SCREEN_START, FILE_DIR

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
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit('QUIT')
            '''
            if event.type == KEYDOWN and event.type == pygame.K_UP:
                up = True
            if event.type == KEYDOWN and event.type == pygame.K_LEFT:
                left = True
            if event.type == KEYDOWN and event.type == pygame.K_RIGHT:
                right = True
            if event.type == KEYDOWN and event.type == pygame.K_LSHIFT:
                running = True
            '''
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    up = True
                if event.type == pygame.K_LEFT:
                    left = True
                if event.type == pygame.K_RIGHT:
                    right = True
                if event.type == pygame.K_LSHIFT:
                    running = True

            if event.type == KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_LSHIFT:
                    running = False

        screen.blit(bg, SCREEN_START)

        monsters.update(platform)
        camera.update()
        hero.uppdate(left, right, up, running, platform)
        for event in entities:
            screen.blit(event.image, camera.apply)

        pygame.display.update()

level = []
platform = []
entities = pygame.sprite.Group()
animatedEntities = pygame.sprite.Group()
monsters = pygame.sprite.Group()

if __name__ == '__main__':
    main()