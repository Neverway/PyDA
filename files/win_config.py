import pygame

pygame.init()
pygame.font.init()

# Resolution edits
display_width = 800
display_height = 600

# Windows resolution
game_display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

# Windows name
pygame.display.set_caption('Divine Annihilation')

# Window icon
window_icon = pygame.image.load('game.png')
pygame.display.set_icon(window_icon)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

isfull = True
