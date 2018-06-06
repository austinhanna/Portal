from kivy.app import App # Import App to build
from kivy.uix.gridlayout import GridLayout # UI elements https://kivy.org/docs/api-kivy.uix.html#module-kivy.uix
from kivy.uix.label import Label # UI elements https://kivy.org/docs/api-kivy.uix.html#module-kivy.uix
from kivy.uix.textinput import TextInput # UI elements https://kivy.org/docs/api-kivy.uix.html#module-kivy.uix

class LoginScreen(GridLayout): # It's a gridlayout because thats our base canvas
    def __init__(self, **kwargs): # Be sure to call **kwargs as well
        super(LoginScreen, self).__init__(**kwargs) # Call super to help implement the function of the original class being overloaded.
        self.cols = 2 # 2 columns
        self.add_widget(Label(text='User Name')) # Add a new widget with help of SUPER, These new widgets are children to the main clas
        self.username = TextInput(multiline=False) # Add some essential properties
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False) # Security property
        self.add_widget(self.password)

class Login(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    Login().run() # Add () after calling main app to run... Login().run() not Login.run()
