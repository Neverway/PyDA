import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

menu_select = pygame.mixer.Sound('loaders/resources/sounds/menu_select.wav')
# effect.play()
# pygame.mixer.music.load('foo.mp3')
# pygame.mixer.music.play(-1)
