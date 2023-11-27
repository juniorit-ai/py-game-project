import pygame
from pygame.surface import Surface

from juniorit.gamecraft.sprite import Sprite
from juniorit.gamecraft.types import *


class Scene:
    children: list[Sprite]
    reDraw: bool

    def __init__(self):
        self.children = []
        self.reDraw = True

    def add_child(self, sprite: Sprite):
        self.children.append(sprite)

    def remove_child(self, sprite: Sprite):
        self.children.remove(sprite)

    def on_update(self, ticks: int):
        for sprite in self.children:
            sprite.on_update(ticks)
            if sprite.reDraw:
                self.reDraw = True

    def on_draw(self, surface: Surface):
        if not self.reDraw:
            return

        for sprite in self.children:
            sprite.on_draw(surface)
            
        pygame.display.flip()
        #pygame.display.update()
        self.reDraw = False

    def on_keyboard(self, event: Event, key_code: int):
        for sprite in self.children:
            sprite.on_keyboard(event, key_code)

    def on_mouse(self, event: Event, point: Point):
        for sprite in self.children:
            sprite.on_mouse(event, point)