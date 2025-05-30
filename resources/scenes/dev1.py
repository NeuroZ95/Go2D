import pygame
from classes.player import Player

player = Player(100, 100)

def Dev1_Update(screen):
    player.Update(screen, (0, 255, 0), 50, 5)