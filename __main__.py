from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from random import random, choice
import time

from kivy.clock import Clock

class BlinkGame(BoxLayout):
    def __init__(self, **kwargs):
        super(BlinkGame, self).__init__(**kwargs)


    def set_color(self, *args):

        rdid=choice([key for key in self.ids.keys()])

        self.ids[rdid].background_color= (0,1,1,1)
        def restore_color(*args):
            self.ids[rdid].background_color=(1,0,1,1)
        Clock.schedule_once(restore_color, 0.2)

    def startgame(self):
        Clock.schedule_interval(self.set_color, 0.5)

class BlinkApp(App):
    def build(self):
        game= BlinkGame()
        game.startgame()
        #print(game.ids.bu7.background_color)
        #print([key for key in game.ids.keys()])
        #print(choice([key for key in game.ids.keys()]))
        return game


if __name__ == "__main__":
    BlinkApp().run()
