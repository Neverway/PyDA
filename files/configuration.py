from divine.run import *

# Variables
last_splash_update = 0
current_splash_frame = 0
dasplash = img.sp1

# Font
render_text2 = "Version 0.0.3"
text_surface2 = font.render(render_text2, False, (255, 255, 255))
menu_id = 1
bar = img.new_game


# Define functions
def splashan(display):
    global last_splash_update
    global current_splash_frame
    global dasplash
    now = pygame.time.get_ticks()

    if now - last_splash_update > 500:
        last_splash_update = now
        if current_splash_frame >= 11:
            frame_2(display)
        current_splash_frame += 1
        dasplash = img.splash.get(current_splash_frame)
    display.blit(dasplash, (200, 200))


def menu(display, x, y):
    global bar
    display.blit(bar, (x, y))
    if menu_id == 1:
        bar = img.new_game
    if menu_id == 2:
        bar = img.load_game
    if menu_id == 3:
        bar = img.quit_game


# Frames
def frame_1(display):
    game_exit = False
    player = Player()
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True
                quit()
            if event.type == pygame.KEYDOWN:
                frame_2(display)

        pygame.display.flip()
        display.blit(background, (0, 0))
        splashan(display)
        clock.tick(30)


def frame_2(display):
    game_exit = False
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True
                quit()

        menu(display, 350, 360)
        display.blit(text_surface2, (10, 5))
        display.blit(img.logo, (170, 250))
        display.blit(img.cright, (600, 570))
        pygame.display.flip()
        display.blit(background, (0, 0))
        clock.tick(30)


def frame_3(display):
    game_exit = False
    player = Player()
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        display.blit(player.image, player.rect)
        pygame.display.flip()
        display.blit(background, (0, 0))
        clock.tick(30)


def frame_4(display):
    game_exit = False
    player = Player()
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        display.blit(player.image, player.rect)
        pygame.display.flip()
        display.blit(background, (0, 0))
        clock.tick(30)
