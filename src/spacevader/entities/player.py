import os

import pygame

from entities.constant import Constant

pygame.init()

class Player:

    def __init__(self):
        self.player_icon = pygame.image.load(Constant.PLAYER_ICON)
        self._player_x = Constant.PLAYER_X_INITIAL
        self.player_y = Constant.PLAYER_Y_INITIAL
        self.player_x_change = Constant.PLAYER_X_CHANGE

    @property
    def player_x(self):
        return self._player_x

    @player_x.setter
    def player_x(self, player_x):
        if player_x <= Constant.LEFT_BOUNDARY:
            self._player_x = Constant.LEFT_BOUNDARY
        elif player_x >= Constant.RIGHT_BOUNDARY:
            self._player_x = Constant.RIGHT_BOUNDARY
        else:
            self._player_x = player_x

    def get_player_change(self, event_type, event_key):
        movement_switcher = {
            pygame.KEYDOWN: {
                pygame.K_LEFT: Constant.PLAYER_X_MOVEMENT_DELTA * -1,
                pygame.K_RIGHT: Constant.PLAYER_X_MOVEMENT_DELTA
            },
            pygame.KEYUP: {
                pygame.K_LEFT: 0,
                pygame.K_RIGHT: 0
            }
        }
        return movement_switcher[event_type].get(event_key)

    def render(self, screen):
        screen.blit(self.player_icon, (self.player_x, self.player_y))