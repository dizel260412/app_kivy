from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from  kivy.uix.button import Button


class LoginScreen(GridLayout):


    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        # self.cols = 2
        # self.add_widget(Label(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        # self.add_widget(Label(text='password'))
        # self.password = TextInput(password=True, multiline=False)
        # self.add_widget(self.password)
        self.layout = GridLayout(cols=5)
        self.layout.add_widget(Button(text='Hello 1'))
        self.layout.add_widget(Button(text='World 1'))
        self.layout.add_widget(Button(text='Hello 2'))
        self.layout.add_widget(Button(text='World 2'))



class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()