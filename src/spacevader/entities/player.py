import pygame

from spacevader.entities.constant import Constant

# pygame.init()

class Player:

    def __init__(self, screen=None):
        # TODO: Evaluate use of meta class
        self._icon = pygame.image.load(Constant.PLAYER_ICON)
        self._x = Constant.PLAYER_X_INITIAL
        self.y = Constant.PLAYER_Y_INITIAL
        self.x_change = Constant.PLAYER_X_CHANGE
        self._screen = screen

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x <= Constant.LEFT_BOUNDARY:
            self._x = Constant.LEFT_BOUNDARY
        elif x >= Constant.RIGHT_BOUNDARY:
            self._x = Constant.RIGHT_BOUNDARY
        else:
            self._x = x

    def delta(self, event_type, event_key):
        movement_switcher = {
            pygame.KEYDOWN: {
                pygame.K_LEFT: Constant.PLAYER_X_MOVEMENT_DELTA * -1,
                pygame.K_RIGHT: Constant.PLAYER_X_MOVEMENT_DELTA
            },
            pygame.KEYUP: {
                pygame.K_LEFT: Constant.PLAYER_X_MOVEMENT_DELTA * 0,
                pygame.K_RIGHT: Constant.PLAYER_X_MOVEMENT_DELTA * 0
            }
        }
        return movement_switcher[event_type].get(event_key)

    def render(self):
        self._screen.blit(self._icon, (self.x, self.y))