from juniorit.gamecraft.scene import Scene
from juniorit.gamecraft.sprite import Sprite

class FirstScene(Scene):
    def __init__(self):
        super().__init__()
        
        sprite = Sprite("t-rex.png")
        self.add_child(sprite)
        
        sprite.set_position(100, 200)

    def on_update(self, ticks: int):
        super().on_update(ticks)
