import random
import math
import os

from pygame import mixer
import pygame

current_dir = os.path.dirname(os.path.realpath(__file__))

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Set background
background = pygame.image.load(os.path.join(current_dir, 'icons/background-2.jpg'))

# Load background sound
mixer.music.load(os.path.join(current_dir, 'sounds/background.wav'))
mixer.music.play(-1)

# Set the score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

score_board_x = 760
score_board_y = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# Set title and icon
pygame.display.set_caption('Spacevader')
# TODO: Check icon visibility in Windows
icon = pygame.image.load(os.path.join(current_dir, 'icons/ufo.png'))
pygame.display.set_icon(icon)

# Player
player_icon = pygame.image.load(os.path.join(current_dir, 'icons/player.png'))
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_icon = pygame.image.load(os.path.join(current_dir, 'icons/enemy.png'))
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
# enemy_x.append(random.randint(0, 736))
# enemy_y.append(random.randint(50, 150))
# enemy_x_change.append(5)
# enemy_y_change.append(40)


# Bullet
bullet_icon = pygame.image.load(os.path.join(current_dir, 'icons/bullet.png'))
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = 'READY'

def show_score(x, y):
    score_value = font.render(f'{score}', True, (255, 255, 255))
    screen.blit(score_value, (x, y))

def player(x, y):
    screen.blit(player_icon, (x, y))

# def init_enemy():
#     enemy_x.append(random.randint(0, 736))
#     enemy_y.append(random.randint(50, 150))
#     enemy_x_change.append(5)
#     enemy_y_change.append(40)

def enemy(x, y):
    screen.blit(enemy_icon, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'FIRE'
    screen.blit(bullet_icon, (x + 16, y + 10))

def has_collided(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    return distance < 27

def game_over_text():
    game_over_text = game_over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))

def run():
    global player_x, player_x_change, player_y
    global enemy_x, enemy_x_change, enemy_y, enemy_y_change
    global bullet_x, bullet_x_change, bullet_y, bullet_y_change, bullet_state
    global score

    running = True
    while running:
        
        # Fill screen with black
        screen.fill((0, 0, 0))

        # Persist background image
        screen.blit(background, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
                if event.key == pygame.K_SPACE and bullet_state is 'READY':
                    bullet_sound = mixer.Sound(os.path.join(current_dir, 'sounds/laser.wav'))
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player_x_change = 0

        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        for i in range(score + 1):

            if len(enemy_x) <= i:
                enemy_x.append(random.randint(0, 736))
                enemy_y.append(random.randint(50, 150))
                enemy_x_change.append(5)
                enemy_y_change.append(40)
                
            # Game over condition
            if enemy_y[i] > 440:
                for j in range(score + 1):
                    enemy_y[j] = 2000
                game_over_text()
                break

            enemy_x[i] += enemy_x_change[i]
            if enemy_x[i] <= 0:
                enemy_x_change[i] = 4
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] = -4
                enemy_y[i] += enemy_y_change[i]

            # Collsion
            collision = has_collided(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision:
                explosion_sound = mixer.Sound(os.path.join(current_dir, 'sounds/explosion.wav'))
                explosion_sound.play()
                bullet_y = 480
                bullet_state = 'READY'
                score += 1
                enemy_x[i] = random.randint(0, 736)
                enemy_y[i] = random.randint(50, 150)

            enemy(enemy_x[i], enemy_y[i])
            

        # Bullet movement
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = 'READY'
        if bullet_state == 'FIRE':
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        # # Collsion
        # collision = has_collided(enemy_x, enemy_y, bullet_x, bullet_y)
        # if collision:
        #     bullet_y = 480
        #     bullet_state = 'READY'
        #     score += 1
        #     enemy_x = random.randint(0, 736)
        #     enemy_y = random.randint(50, 150)

        player(player_x, player_y)
        # for i in range(score + 1):
            # enemy(enemy_x[i], enemy_y[i])
        show_score(score_board_x, score_board_y)
        pygame.display.update()

if __name__ == '__main__':
    run()