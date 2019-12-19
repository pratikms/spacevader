import pygame
import random

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Set background
background = pygame.image.load('icons/background-2.jpg')

# Set title and icon
pygame.display.set_caption('spacevader')
# TODO: Check icon visibility in Windows
icon = pygame.image.load('icons/ufo.png')
pygame.display.set_icon(icon)

# Player
player_icon = pygame.image.load('icons/player.png')
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_icon = pygame.image.load('icons/enemy.png')
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 5
enemy_y_change = 40

# Bullet
bullet_icon = pygame.image.load('icons/bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = 'READY'

def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y):
    screen.blit(enemy_icon, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'FIRE'
    screen.blit(bullet_icon, (x + 16, y + 10))

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
        
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 4
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -4
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'READY'
    if bullet_state == 'FIRE':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        # bullet_state = 'READY'

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()