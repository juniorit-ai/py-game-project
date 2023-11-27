import pygame
from pygame.surface import Surface
import asyncio
from juniorit.gamecraft.scene import Scene
from juniorit.gamecraft.types import *

class Game:
    _instance = None
    
    GAME_FPS = 60
    
    surface:Surface = None
    
    scenes: list[Scene]
    current_scene: Scene

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance

    def init(self, width: int, height: int, caption: str = "JuniorIT.AI Game Craft"):
        self.width = width
        self.height = height
        self.scenes = []
        self.current_scene = None
        self.running = False

        pygame.init()
        pygame.display.set_caption(caption)

        self.surface = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

    def add_scene(self, scene: Scene):
        self.scenes.append(scene)

    def remove_scene(self, scene: Scene):
        self.scenes.remove(scene)

    def set_current_scene(self, scene: Scene):
        self.current_scene = scene

    def on_update(self):
        self.process_events()
        
        frame_start = pygame.time.get_ticks()
        ticks = 1000 // self.GAME_FPS
        
        if self.current_scene is not None:
            self.current_scene.on_update(ticks)
            self.current_scene.on_draw(self.surface)
            
        frame_time = pygame.time.get_ticks() - frame_start
        if ticks > frame_time:
            pygame.time.delay(ticks - frame_time)

    def map_event(self, pygame_event_type):
        return Event(pygame_event_type) if pygame_event_type in Event._value2member_map_ else Event.UNKNOWN
    
    def process_events(self):
        for event in pygame.event.get():
            event_type = self.map_event(event.type)
            if event_type in [Event.KEYDOWN, Event.KEYUP]:
                self.on_keyboard(event_type, event.key)
            elif event_type == Event.MOUSEWHEEL:
                point = Point(event.x, event.y)
                self.on_mouse(event_type, point)
            elif event_type in [Event.MOUSEMOTION, Event.MOUSEBUTTONDOWN, Event.MOUSEBUTTONUP]:
                point = Point(event.pos[0], event.pos[1])
                self.on_mouse(event_type, point)
            elif event.type == pygame.QUIT:
                self.running = False
                # Optionally handle SDL_QUIT like behavior here
            else:
                # Handle other events or unknown events
                pass
            
    def on_keyboard(self, event: Event, key_code: int):
        if key_code == pygame.K_ESCAPE:
            self.running = False
            # Optionally trigger a quit event
        if self.current_scene:
            self.current_scene.on_keyboard(event, key_code)


    def on_mouse(self, event: Event, point: Point):
        if self.current_scene:
            self.current_scene.on_mouse(event, point)

    async def main_loop(self):
        
        while self.running:
            self.on_update()
            await asyncio.sleep(0)
            
        pygame.quit()

    def run(self):
        self.running = True
        asyncio.run(self.main_loop())
