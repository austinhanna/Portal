import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
Window.fullscreen = 'auto'

class Clok(Label):
    def update(self, *args):
        self.text = time.asctime()

class TimeApp(App):
    def build(self):
        crudeclock = Clok()
        Clock.schedule_interval(crudeclock.update, 1)
        return crudeclock

if __name__ == "__main__":
    TimeApp().run()
