from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        fl = FloatLayout(size=(300, 300))
        fl.add_widget(Button(text='Hello',
                             font_size=16,
                             on_press=self.btn_press,
                             background_color=[1, 0, 0, 1],
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(0, 0)
                             ))
        return fl

    def btn_press(self, instance):
        print('Cliked')
        instance.background_color = [.23, .29, .5, 1]


if __name__ == '__main__':
    MyApp().run()
