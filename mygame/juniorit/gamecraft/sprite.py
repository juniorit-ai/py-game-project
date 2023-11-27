import pygame
from pygame.surface import Surface
from juniorit.gamecraft.utils import get_resource_file_path
from juniorit.gamecraft.types import *

class Sprite:
    
    def __init__(self, image_file: str, frames: list[Rect] = None):
        
        image_path = get_resource_file_path(image_file)
        
        self.reDraw = True
        
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.frames = frames or []
        self.frame_index = 0
        
        self.top = 0.0
        self.left = 0.0
        self.scale = 1.0
        self.angle = 0.0
        self.center = (0, 0)
        self.flip = FlipMode.FLIP_NONE
        self.reDraw = True

    def set_position(self, top: float, left: float):
        self.top = top
        self.left = left
        self.reDraw = True
        
    def set_scale(self, scale: float):
        self.scale = scale
        self.reDraw = True

    def set_angle(self, angle: float):
        self.angle = angle
        self.reDraw = True
        
    def set_center(self, center):
        self.center = center
        self.reDraw = True
        
    def set_flip(self, flip_mode: FlipMode):
        self.flip = flip_mode
        self.reDraw = True
        
    def set_frame(self, frame_index: int):
        if 0 <= frame_index < len(self.frames):
            self.frame_index = frame_index
            self.reDraw = True

    def on_update(self, ticks: int):
        # Update logic here
        pass

    def on_draw(self, surface: Surface):
        if self.frames:
            frame = self.frames[self.frame_index]
            image = self.image.subsurface(pygame.Rect(frame.x, frame.y, frame.w, frame.h))
        else:
            image = self.image

        image = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height * self.scale)))
        image = pygame.transform.rotate(image, self.angle)

        flip_horizontal = self.flip == FlipMode.FLIP_HORIZONTAL or self.flip == FlipMode.FLIP_DIAGONAL
        flip_vertical = self.flip == FlipMode.FLIP_VERTICAL or self.flip == FlipMode.FLIP_DIAGONAL
        image = pygame.transform.flip(image, flip_horizontal, flip_vertical)

        surface.blit(image, (self.left, self.top))
        self.reDraw = False
        
    def on_keyboard(self, event: Event, key_code: int):
        # Keyboard event handling
        pass

    def on_mouse(self, event: Event, point: Point):
        # Mouse event handling
        pass
