import logging

import pygame
from pygame.locals import *


log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
clock = pygame.time.Clock()


def create_surface():
    pass


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('loaders/resources/sprites/ent_char_right.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()


class Player(Mob):
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


def create_display(height=600, width=800, title=True):
    """
    Create a PyGame display.

    :param height: Vertical resolution in pixels
    :param width: Horizontal resolution in pixels
    :param title: Window title
    :return: A PyGame display object
    """
    display = pygame.display.set_mode((width, height))
    try:
        pygame.display.set_caption(title)
    except TypeError:
        log.debug("Using default title")
    return display


def game_loop(display):
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


def main():
    """Run the program."""
    # Set window resolution
    display_width = 800
    display_height = 600

    pygame.init()
    display = create_display(display_height, display_width, 'Divine')
    game_loop(display)
    pygame.quit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
