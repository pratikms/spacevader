import pygame

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Set title and icon
pygame.display.set_caption('Spacevaders')
# TODO: Check icon visibility in Windows
icon = pygame.image.load('icons/ufo.png')
pygame.display.set_icon(icon)

# Player
player_icon = pygame.image.load('icons/player.png')
player_x = 370
player_y = 480
player_x_change = 0

def player(x, y):
    screen.blit(player_icon, (x, y))

running = True
while running:
    
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0

    player_x += player_x_change
    player(player_x + player_x_change, player_y)
    pygame.display.update()