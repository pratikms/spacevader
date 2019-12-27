import os
from itertools import count
import math

import pygame

from entities.constant import Constant

class Alien:

    _ids = count(0)

    def __init__(self, x=None, y=None, x_change=None, y_change=None):
        self.id = next(self._ids)
        self._icon = pygame.image.load(Constant.ALIEN_ICON)
        self._x = x
        self._y = y
        self.x_change = x_change
        self._y_change = y_change
        self.invaded = False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        # print(self.y, self._y_change)
        if x <= Constant.LEFT_BOUNDARY:
            self.x_change = Constant.ALIEN_X_MOVEMENT_DELTA
            self.y += self._y_change
            # print(self.y, self._y_change)
        elif self._x >= Constant.RIGHT_BOUNDARY:
            print(f'x_change: {self.x_change}')
            self.x_change = Constant.ALIEN_X_MOVEMENT_DELTA * -1
            print(f'x_change: {self.x_change}')
            self.y += self._y_change
            # print(self.y, self._y_change)
        # print()
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        print(self.y, self._y_change)
        print(f'Setter: {y}')
        self._y = y
        print(self.y, self._y_change)
        print()
        if self._y > Constant.INVADE_BOUNDARY:
            self.invaded = True

    def game_over(self, screen):
        game_over_font = pygame.font.Font(Constant.GAME_OVER_FONT_TYPE, Constant.GAME_OVER_FONT_SIZE)
        game_over_text = game_over_font.render('GAME OVER', True, (255, 255, 255))
        screen.blit(game_over_text, (Constant.GAME_OVER_X, Constant.GAME_OVER_Y))

    def has_collided(self, bullet_x, bullet_y):
        distance = math.sqrt(math.pow(self._x - bullet_x, 2) + math.pow(self._y - bullet_y, 2))
        return distance < Constant.COLLISION_DELTA

    def render(self, screen):
        screen.blit(self._icon, (self._x, self._y))
