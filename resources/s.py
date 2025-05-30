import pygame
from classes.player import Player

player = Player(0, 0)

def DeclScene_Dev1():
    player = Player(100, 100)

def UpdateScene_Dev1(screen):
    player.Update(screen, (0, 255, 0), 50, 5)