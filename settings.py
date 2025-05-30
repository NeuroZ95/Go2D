import pygame

pygame.mixer.init()

# WINDOW PARAMETERS

WINDOW_SIZE = (1360, 720)

WINDOW_CAPTION = "Go1D"

WINDOW_ICON = pygame.image.load("icon.ico")

# TEXTURES/IMAGES

T_testSpec = pygame.image.load("resources/sprites/testSpec.jpg")
I_testSpec = pygame.transform.scale(T_testSpec, WINDOW_SIZE)

T_joyer_red = pygame.image.load("resources/sprites/joyer_red.png")
I_joyer_red = pygame.transform.scale(T_joyer_red, WINDOW_SIZE)

# SOUNDS

S_punch1 = pygame.mixer.Sound("resources/sounds/punch1.mp3")
