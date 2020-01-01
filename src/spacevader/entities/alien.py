from itertools import count
import math
import random

from pygame import mixer
import pygame

from spacevader.entities.constant import Constant

class Alien:

    _ids = count(0)

    def __init__(self, x=None, y=None, x_change=None, y_change=None, screen=None):
        self.id = next(self._ids)
        self._icon = pygame.image.load(Constant.ALIEN_ICON)
        self._x = x
        self._y = y
        self.x_change = x_change
        self._y_change = y_change
        self._screen = screen
        self.invaded = False

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x <= Constant.LEFT_BOUNDARY:
            self.x_change = Constant.ALIEN_X_MOVEMENT_DELTA
            self.y += self._y_change
        elif x >= Constant.RIGHT_BOUNDARY:
            self.x_change = Constant.ALIEN_X_MOVEMENT_DELTA * -1
            self.y += self._y_change
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        if self._y > Constant.INVADE_BOUNDARY:
            self.invaded = True

    @classmethod
    def game_over(cls, screen):
        game_over_font = pygame.font.Font(Constant.FONT, Constant.GAME_OVER_FONT_SIZE)
        game_over_text = game_over_font.render('GAME OVER', True, (255, 255, 255))
        screen.blit(game_over_text, (Constant.GAME_OVER_X, Constant.GAME_OVER_Y))

        restart_icon = pygame.image.load(Constant.RESTART_ICON)
        screen.blit(restart_icon, (Constant.RESTART_X, Constant.RESTART_Y))

    def has_collided(self, bullet):
        distance = math.sqrt(math.pow(self._x - bullet.x, 2) + math.pow(self._y - bullet.y, 2))
        return distance < Constant.COLLISION_DELTA

    def explode(self, bullet):
        explosion_sound = mixer.Sound(Constant.EXPLOSION_SOUND)
        explosion_sound.play()
        # TODO: Check if this is necessary for NORMAL mode
        self.x = random.randint(Constant.LEFT_BOUNDARY, Constant.RIGHT_BOUNDARY)
        self.y = random.randint(Constant.ALIEN_SPAWN_TOP_BOUNDARY, Constant.ALIEN_SPAWN_BOTTOM_BOUNDARY)
        bullet.y = Constant.BULLET_Y_INITIAL
        bullet.state = 'READY'

    def render(self):
        self._screen.blit(self._icon, (self._x, self._y))

    @classmethod
    def dispose(cls, aliens):
        for alien in aliens:
            alien.y = 2000
