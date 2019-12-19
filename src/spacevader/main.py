import pygame
import random

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

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
enemy_x_change = 0.5
enemy_y_change = 40

def player(x, y):
    screen.blit(player_icon, (x, y))

def enemy(x, y):
    screen.blit(enemy_icon, (x, y))

running = True
while running:
    
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5

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
        enemy_x_change = 0.5
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.5
        enemy_y += enemy_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()