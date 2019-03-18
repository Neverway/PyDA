import pygame
from files import text_lines as tl, img_load as img
import os
path = os.path.abspath("frames/retro.ttf")

global win

pygame.init()
pygame.font.init()

# Resolution edits
display_width = 800
display_height = 600

# Windows resolution
win = pygame.display.set_mode((display_width, display_height))

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

isfull = False


# Game font
font = pygame.font.SysFont('Courier New', 20)
font2 = pygame.font.Font(path, 12)
font3 = pygame.font.Font(path, 16)

clock = pygame.time.Clock()
line_count = 1
script = tl.fail_safe.get(1)
render_text = script
render_text2 = "BLANK UNTIL OVERWRITE"
text_surface = font.render(render_text, True, (255, 255, 255))
text_surface2 = font2.render(render_text2, False, (255, 255, 255))
