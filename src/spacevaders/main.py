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

def player():
    screen.blit(player_icon, (player_x, player_y))

running = True
while running:
    
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()