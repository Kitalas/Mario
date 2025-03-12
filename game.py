import os

import pygame

from block import game_map

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
REAL_WIDTH = 50 * len(game_map[0])

bg_image = pygame.image.load(
    os.path.join(
        os.path.abspath(__file__ + "/.."),
        "bg.png"
    )
)
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

offset_x = 0
offset_y = -400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def map_generator(game_map):
    x = 0
    y = 0
    for row in game_map:
        for item in row:
            if item == "1":
                yield Block(x, y, 50, 50, 'block.png')
            x += 50
        y += 50
        x = 0


class Sprite(pygame.Rect):
    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            image_name: str,
    ):
        super().__init__(x, y, width, height)
        self.is_active = True
        self.image_name = image_name
        self.image = None
        self._load_image()

    def _load_image(self):
        image = pygame.image.load(
            os.path.join(
                os.path.abspath(__file__ + "/.."),
                self.image_name
            )
        )
        transformed_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = transformed_image

    @property
    def bottom_y(self):
        return self.y + self.height

    @property
    def right_x(self):
        return self.x + self.width

    def _draw(self):
        screen.blit(self.image, (self.x, self.y))

    def _move(self):
        pass

    def _gravity(self):
        pass

    def process(self):
        if self.is_active:
            self._draw()
            self._move()
            self._gravity()

class Block(Sprite):
    block_list = []

    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)
        self.x_static = self.x
        self.y_static = self.y

    @classmethod
    def get_block_list(cls):
        return [item for item in cls.block_list if item.is_active]

    @classmethod
    def init(cls):
        cls.block_list = [block for block in map_generator(game_map)]

    def collide_hero_up(self):
        if self.colliderect(main_hero):
            if self.y >= main_hero.bottom_y - 2:
                return True

    def collide_hero_left(self):
        if self.colliderect(main_hero):
            if self.x <= main_hero.right_x and main_hero.x < self.x and not self.y >= main_hero.bottom_y - 2:
                return True

    def collide_hero_right(self):
        if self.colliderect(main_hero):
            if self.right_x >= main_hero.x and main_hero.right_x > self.right_x and not self.y >= main_hero.bottom_y - 2:
                return True

    def _draw(self):
        screen.blit(self.image, (self.x, self.y))

    @classmethod
    def all_block_process(cls):
        for block in cls.block_list:
            block.process()

    def _move(self):
        self.x = self.x_static - offset_x
        self.y = self.y_static - offset_y


class Block(Sprite):
    block_list = []

    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)
        self.x_static = self.x
        self.y_static = self.y

    @classmethod
    def get_block_list(cls):
        return [item for item in cls.block_list if item.is_active]

    @classmethod
    def init(cls):
        cls.block_list = [block for block in map_generator(game_map)]

    def collide_hero_up(self):
        if self.colliderect(main_hero):
            if self.y >= main_hero.bottom_y - 2:
                return True

    def collide_hero_left(self):
        if self.colliderect(main_hero):
            if self.x <= main_hero.right_x and main_hero.x < self.x and not self.y >= main_hero.bottom_y - 2:
                return True

    def collide_hero_right(self):
        if self.colliderect(main_hero):
            if self.right_x >= main_hero.x and main_hero.right_x > self.right_x and not self.y >= main_hero.bottom_y - 2:
                return True

    def _draw(self):
        screen.blit(self.image, (self.x, self.y))

    @classmethod
    def all_block_process(cls):
        for block in cls.block_list:
            block.process()

    def _move(self):
        self.x = self.x_static - offset_x
        self.y = self.y_static - offset_y


class Hero(Sprite):
    def __init__(self, x, y, width, height, image_name):
        super().__init__(x, y, width, height, image_name)
        self.gravity_speed = 1
        self.gravity_active = True
        self.speed = 1

        self.jump_speed = 1.5
        self.jump_active = False
        self.jump_counter_default = 80
        self.jump_counter_current = self.jump_counter_default

        self.reload_counter_default = 100
        self.reload_counter_current = self.reload_counter_default

    def _gravity(self):
        global offset_y
        self.gravity_active = not self._is_on_floor()
        if self.gravity_active and not self.jump_active:
            offset_y += self.gravity_speed
            self.y += self.gravity_speed

        self.gravity_active = True

    def _move(self):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_LEFT]:
            self._move_left()
        if keyboard[pygame.K_RIGHT]:
            self._move_right()
        if keyboard[pygame.K_UP]:
            self._start_jump()
        if keyboard[pygame.K_SPACE]:
            self._strike()

    def _is_on_floor(self):
        if any([block.collide_hero_up() for block in Block.get_block_list()]):
            return True

    def _start_jump(self):
        if self._is_on_floor() and not self.jump_active:
            self.jump_active = True

    def _jump_process(self):
        global offset_y
        if self.jump_active:
            if self.jump_counter_current != 0:
                self.jump_counter_current -= 1
                offset_y -= self.jump_speed
                self.y -= self.jump_speed
            else:
                self.jump_counter_current = self.jump_counter_default
                self.jump_active = False

    def _move_right(self):
        global offset_x
        if self.right_x < SCREEN_WIDTH and not any([block.collide_hero_left() for block in Block.get_block_list()]):
            if offset_x >= REAL_WIDTH - SCREEN_WIDTH:
                self.x += self.speed
            elif self.x >= SCREEN_WIDTH // 2:
                offset_x += self.speed
            else:
                self.x += self.speed

    def _move_left(self):
        global offset_x
        if self.x > 0 and not any([block.collide_hero_right() for block in Block.get_block_list()]):
            if offset_x <= 0:
                self.x -= self.speed
            elif self.x >= SCREEN_WIDTH // 2:
                self.x -= self.speed
            else:
                offset_x -= self.speed

    def _strike(self):
        if self.reload_counter_current == 0:
            self.reload_counter_current = self.reload_counter_default
        else:
            self.reload_counter_current -= 1

    def process(self):
        super().process()
        self._jump_process()


main_hero = Hero(40, 40, 40, 50, 'Kitalas.png')
Block.init()


def start_game():
    game_run = True

    while game_run:
        screen.blit(bg_image, (0, 0))
        main_hero.process()
        Block.all_block_process()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

        pygame.display.flip()


start_game()

# ono bez settings