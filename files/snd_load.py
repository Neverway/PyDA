from files.config import *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

menu_select = pygame.mixer.Sound('sounds/menu_select.wav')
# effect.play()
# pygame.mixer.music.load('foo.mp3')
# pygame.mixer.music.play(-1)
