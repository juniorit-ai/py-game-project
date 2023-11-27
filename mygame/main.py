from juniorit.gamecraft.game import Game
from first_scene import FirstScene

def app():
    
    width = 1280
    height = 512
    
    print(f'"Game starts; Scene width: {width}, height: {height}')
    
    game = Game.instance()
    game.init(width, height)
    
    scene = FirstScene()
    game.add_scene(scene)
    
    game.set_current_scene(scene)
    
    game.run()

if __name__ == "__main__":
    
    app()
