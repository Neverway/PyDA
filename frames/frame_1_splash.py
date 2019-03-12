from Divine_Annihilation import *
from files import text_lines as tl, win_config as win, img_load as img
import os
path = os.path.abspath("frames/retro.ttf")

# This is important and needs to be first
pygame.init()
pygame.font.init()
# Font
# Font
render_text2 = "Loading.."
font2 = pygame.font.Font(path, 12)
text_surface2 = font2.render(render_text2, False, (255, 255, 255))


tl = tl


def splash(x, y):
    win.game_display.blit(img.splash, (x, y))


def debug():
    pass


#######################
def pyupdate():
    splash(200, 200)
    win.game_display.blit(text_surface2, (150, 400))
    pygame.display.update()
#######################


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            debug()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pass

    # End group
        win.game_display.fill(win.black)
        pygame.mouse.set_visible(False)
        pyupdate()
        pygame.time.wait(2000)
        from frames import frame_2_main
        frame_2_main = frame_2_main
        pygame.display.update()


game_loop()
pygame.quit()
quit()
