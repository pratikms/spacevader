from pygame import mixer
import pygame

from spacevader.entities.constant import Constant

class Bullet:

    def __init__(self, screen=None):
        self._icon = pygame.image.load(Constant.BULLET_ICON)
        self.x = Constant.BULLET_X_INITIAL
        self.y = Constant.BULLET_Y_INITIAL
        self._x_change = Constant.BULLET_X_CHANGE
        self._y_change = Constant.BULLET_Y_CHANGE
        self.state = 'READY'
        self._screen = screen

    def fire(self, sound=False):
        if sound:
            bullet_sound = mixer.Sound(Constant.BULLET_SOUND)
            bullet_sound.play()
        self.state = 'FIRE'
        self._screen.blit(self._icon, (self.x + 16, self.y + 10))