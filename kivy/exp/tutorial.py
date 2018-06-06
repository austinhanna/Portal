import kivy

from kivy.app import App # imports
from kivy.uix.label import Label # Label as in a design element. UIX documentation

class Tutorial(App): # This is where we are defining the Base Class of our Kivy App. You should only ever need to change the name of your app MyApp in this line.
    def build(self): # Initialize 'root' widget aka first class? Kivy app lifecycle
        return Label(text='Austin wrote his first shit congrats\nlmao') # Simple label text

if __name__ == '__main__': # This initializes the app and lets us run it
    Tutorial().run() # Run the application "Tutorial" must be the same name as the root class that builds the program.
