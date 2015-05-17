from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, NumericProperty, StringProperty, ObjectProperty, ListProperty
from kivy.utils import get_random_color
from kivy.storage.jsonstore import JsonStore
from random import random, choice
import time
from datetime import datetime


class Homescreen(Screen):
    pass


class ScoreScreen(Screen):
    scoreslist = ListProperty()


class BlinkButton(Button):
    blinking = BooleanProperty(False)

    def win_or_not(self):
        myapp = App.get_running_app()
        if self.blinking:
            myapp.SCORE += 1
            print("you win " + str(myapp.SCORE))
        else:
            print("try again")


class BlinkGame(Screen):
    TIMER = NumericProperty(10)
    game_is_running = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(BlinkGame, self).__init__(**kwargs)

    def set_color(self, *args):
        rdid = choice([key for key in self.ids.keys()])
        self.ids[rdid].background_color = (get_random_color())
        self.ids[rdid].blinking = True

        def restore_color(*args):
            self.ids[rdid].background_color = (0.6, 0.937, 0.133, 1)
            self.ids[rdid].blinking = False
        Clock.schedule_once(restore_color, 0.4)

    def startgame(self):
        myapp = App.get_running_app()
        if not self.game_is_running:
            self.game_is_running = True
            self.TIMER = 10
            myapp.SCORE = 0
            Clock.schedule_interval(self.set_color, 0.5)
            Clock.schedule_once(self.stopgame, 20)
            Clock.schedule_interval(self.updatetimer, 1)
        else:
            pass

    def stopgame(self, *args):
        Clock.unschedule(self.set_color)
        Clock.unschedule(self.updatetimer)
        myapp = App.get_running_app()
        self.game_is_running = False
        self.TIMER = 0
        myapp.save()
        box = BoxLayout(orientation='vertical')
        mybutton = Button(text='Close me !', size_hint=(1, 0.3))
        box.add_widget(Label(text='Time over, your score is {}'.format(myapp.SCORE)))
        box.add_widget(mybutton)
        popup = Popup(title='BlinkGame', content=box, size_hint=(0.5, 0.5), auto_dismiss=False)
        mybutton.bind(on_press = popup.dismiss)
        popup.open()

    def updatetimer(self, TIMER):
        if self.TIMER == 0:
            self.stopgame()
        else:
            self.TIMER -= 1


class BlinkApp(App):
    store = JsonStore("Scores.json")
    SCORE = NumericProperty(0)

    def save(*args):
        dt = datetime.now().strftime("%d-%b-%y ; %H:%M")
        myapp = App.get_running_app()
        myapp.store.put(dt, score=myapp.SCORE)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Homescreen(name='home'))
        sm.add_widget(BlinkGame(name='game'))
        sm.add_widget(ScoreScreen(name='scorescreen'))
        return sm


if __name__ == "__main__":
    BlinkApp().run()
