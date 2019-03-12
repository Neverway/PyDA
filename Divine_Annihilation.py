import pygame
from frames import frame_1_splash
from files import text_lines as tl, win_config as win
# This is important and needs to be first
pygame.init()
pygame.font.init()
# Game font
font = pygame.font.SysFont('Courier New', 20)
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# Game clock(FPS)
clock = pygame.time.Clock()
line_count = 1
script = tl.failsafe.get(1)
render_text = script
text_surface = font.render(render_text, True, (255, 255, 255))
frame_1_splash = frame_1_splash
win = win


def controls():
    fullscreen = 'F1'
    # Constant
    global isfull
    #if event.type == pygame.KEYDOWN:
     #   if event.key == pygame.K_(fullscreen) and not win.isfull:
     #       win.game_display = pygame.display.set_mode((win.display_width, win.display_height), pygame.FULLSCREEN)
     #       win.isfull = True
     #   if event.key == pygame.K_ESCAPE and win.isfull:
     #       win.game_display = pygame.display.set_mode((win.display_width, win.display_height))
     #       win.isfull = False
     #   if event.key == pygame.K_F4:
     #       game_exit = True


#######################
def pyupdate():
    pass
#######################
