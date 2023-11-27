import pygame
from enum import Enum

class Event(Enum):
    KEYDOWN = pygame.KEYDOWN
    KEYUP = pygame.KEYUP
    MOUSEWHEEL = pygame.MOUSEWHEEL
    MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
    MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
    MOUSEMOTION = pygame.MOUSEMOTION
    UNKNOWN = None

class FlipMode(Enum):
    FLIP_NONE = None
    FLIP_HORIZONTAL = 1
    FLIP_VERTICAL = 2
    FLIP_DIAGONAL = 3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
