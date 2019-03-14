from Divine_Annihilation import *
from files import text_lines as tl, win_config as win, img_load as img
import os
path = os.path.abspath("frames/retro.ttf")

# This is important and needs to be first
pygame.init()
pygame.font.init()
# Font
# Font
render_text2 = "Loading..."
font2 = pygame.font.Font(path, 12)
text_surface2 = font2.render(render_text2, False, (255, 255, 255))
last_splash_update = 0
current_splash_frame = 0
dasplash = img.sp1
loop = True

tl = tl


def splashan():
    global last_splash_update
    global current_splash_frame
    global dasplash

    now = pygame.time.get_ticks()

    if now - last_splash_update > 500:
        last_splash_update = now
        if current_splash_frame >= 11:
            from frames import frame_2_main
            frame_2_main = frame_2_main
        current_splash_frame += 1
        dasplash = img.splash.get(current_splash_frame)
    win.game_display.blit(dasplash, (200, 200))


def debug():
    pass


#######################
def pyupdate():
    splashan()
    win.game_display.blit(text_surface2, (600, 570))
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
                from frames import frame_2_main

    # End group
        win.game_display.fill(win.black)
        pygame.mouse.set_visible(False)
        pyupdate()


game_loop()
pygame.quit()
quit()
