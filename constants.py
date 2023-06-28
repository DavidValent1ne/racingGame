import pygame
from pathlib import Path
from typing import Callable

NAME = 'Racing Game'

SPRITES = "sprites/"


pygame.display.init()
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE)

Coordinate = tuple[int, int]
RGB = tuple[int, int, int]
Rect = tuple[int, int, int, int]
Function = Callable[[], None]

FPS = 60


