from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.player = Rectangle(pos=(100, 100), size=(80, 80))

    def on_touch_move(self, touch):
        self.player.pos = (touch.x - 40, touch.y - 40)

class MyGame(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    MyGame().run()
  
