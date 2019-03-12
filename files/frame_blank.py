from Divine_Annihilation import *
from files import text_lines as tl, win_config as win, img_load as img


def debug():
 pass


#######################
def pyupdate():
    pass
#######################


def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
