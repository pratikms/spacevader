import os

class Constant:

    CURR_DIR = os.path.dirname(os.path.realpath(__file__))

    GAME_NAME = 'Spacevader'
    GAME_ICON = os.path.join(f'{CURR_DIR}/../', 'icons/ufo.png')

    LEFT_BOUNDARY = 0
    RIGHT_BOUNDARY = 736
    INVADE_BOUNDARY = 440

    BACKGROUND_ICON = os.path.join(f'{CURR_DIR}/../', 'icons/background-2.jpg')
    BACKGROUND_SOUND = os.path.join(f'{CURR_DIR}/../', 'sounds/background.wav')

    FONT = 'freesansbold.ttf'

    PLAYER_ICON = os.path.join(f'{CURR_DIR}/../', 'icons/player.png')
    PLAYER_X_INITIAL = 370
    PLAYER_Y_INITIAL = 480
    PLAYER_X_CHANGE = 0
    PLAYER_X_MOVEMENT_DELTA = 7

    ALIEN_ICON = os.path.join(f'{CURR_DIR}/../', 'icons/alien.png')
    ALIEN_X_MOVEMENT_DELTA = 4
    ALIEN_SPAWN_TOP_BOUNDARY = 50
    ALIEN_SPAWN_BOTTOM_BOUNDARY = 150

    EXPLOSION_SOUND = os.path.join(f'{CURR_DIR}/../', 'sounds/explosion.wav')

    COLLISION_DELTA = 27

    GAME_OVER_FONT_SIZE = 64
    GAME_OVER_X = 200
    GAME_OVER_Y = 250

    RESTART_ICON = os.path.join(f'{CURR_DIR}/../', 'icons/restart.png')
    RESTART_X = 370
    RESTART_Y = GAME_OVER_Y + GAME_OVER_FONT_SIZE + 15
    
    BULLET_ICON = os.path.join(f'{CURR_DIR}/../', 'icons/bullet.png')
    BULLET_X_INITIAL = 0
    BULLET_Y_INITIAL = 480
    BULLET_X_CHANGE = 0
    BULLET_Y_CHANGE = 20
    BULLET_SOUND = os.path.join(f'{CURR_DIR}/../', 'sounds/laser.wav')

    SCORE_BOARD_X = 750
    SCORE_BOARD_Y = 10
    