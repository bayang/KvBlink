from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from random import random, choice
import time


class Homescreen(Screen):
    pass


class BlinkButton(Button):
    blinking = BooleanProperty(False)
    def win_or_not(self):
        if self.blinking:
            popup = Popup(title='Win', content=Label(text='You win'), size_hint=(0.5, 0.5))
            popup.open()
            print("you win")
        else:
            print("try again")


class BlinkGame(Screen):
    def __init__(self, **kwargs):
        super(BlinkGame, self).__init__(**kwargs)

    def set_color(self, *args):

        rdid = choice([key for key in self.ids.keys()])
        self.ids[rdid].background_color = (0, 1, 1, 1)
        self.ids[rdid].blinking = True

        def restore_color(*args):
            self.ids[rdid].background_color = (1, 0, 1, 1)
            self.ids[rdid].blinking = False
        Clock.schedule_once(restore_color, 0.4)

    def startgame(self):
        game_is_running = False
        if not game_is_running:
            Clock.schedule_interval(self.set_color, 0.5)
            game_is_running = True
        else:
            pass

    def stopgame(self):
        Clock.unschedule(self.set_color)


class BlinkApp(App):
    def build(self):
        #print(game.)
        #print([key for key in game.ids.keys()])
        #print(choice([key for key in game.ids.keys()]))
        sm = ScreenManager()
        sm.add_widget(Homescreen(name='home'))
        sm.add_widget(BlinkGame(name='game'))
        return sm


if __name__ == "__main__":
    BlinkApp().run()
