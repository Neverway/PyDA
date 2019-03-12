from Divine_Annihilation import *
from files import text_lines as tl, win_config as win, img_load as img
import os
path = os.path.abspath("frames/retro.ttf")

# This is important and needs to be first
pygame.init()
pygame.font.init()
# Game font

font = pygame.font.SysFont('Courier New', 20)
font2 = pygame.font.Font(path, 12)

player_name = "Dev_1"
tl = tl
img = img


def hud_hp_shelf():
    win.game_display.blit(img.hp_shelf, (0, 0))
    name_text = font2.render(player_name, False, (255, 255, 255))
    win.game_display.blit(name_text, (2, 4))


def chat_text():
    global text_surface
    text_surface = font.render(render_text, True, (255, 255, 255))
    win.game_display.blit(text_surface, (10, 483))


def chatbar():
    win.game_display.blit(img.chtbar, (0, 473))
    chat_text()


def debug():
    pass


#######################
def pyupdate():
    chatbar()
#######################


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            global isfull
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and not win.isfull:
                    win.game_display = pygame.display.set_mode((win.display_width, win.display_height), pygame.FULLSCREEN)
                    win.isfull = True
                if event.key == pygame.K_F1 and win.isfull:
                    win.game_display = pygame.display.set_mode((win.display_width, win.display_height))
                    win.isfull = False
                if event.key == pygame.K_ESCAPE:
                    game_exit = True

            debug()

    # End group
        win.game_display.fill(win.black)
        pyupdate()
        pygame.display.update()
    clock.tick(30)


game_loop()
pygame.quit()
quit()
