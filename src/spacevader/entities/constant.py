import os

class Constant:

    CURR_DIR = os.path.dirname(os.path.realpath(__file__))

    LEFT_BOUNDARY = 0
    RIGHT_BOUNDARY = 736

    PLAYER_ICON = os.path.join(f'{CURR_DIR}/../', 'icons/player.png')
    PLAYER_X_INITIAL = 370
    PLAYER_Y_INITIAL = 480
    PLAYER_X_CHANGE = 0
    PLAYER_X_MOVEMENT_DELTA = 5