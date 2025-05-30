import pygame

from resources.scenes.dev1 import Dev1_Update
from settings import *
from classes.player import Player
import resources.scenes.dev1

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)
pygame.display.set_icon(WINDOW_ICON)

clock = pygame.time.Clock()

isRun = True
while isRun:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            isRun = False

    screen.fill((0, 0, 0))

    screen.blit(I_testSpec, (0, 0))

    Dev1_Update(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
