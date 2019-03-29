import logging

import pygame
from pygame.locals import *

from divine.loaders import images as img
from files import configuration as conf

# Variables
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
clock = pygame.time.Clock()
character_image = img.char_right


# Classes
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = character_image.convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()


class Player(Mob):
    def update(self, pressed_keys):
        global character_image
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)
            character_image = img.char_up
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
            character_image = img.char_down
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)


# Define functions
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


# Run program
def main():
    """Run the program."""
    # Set window resolution
    display_width = 800
    display_height = 600

    pygame.init()
    display = create_display(display_height, display_width, 'Divine')
    conf.frame_1(display)
    pygame.quit()


# Keep program from running on import
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
