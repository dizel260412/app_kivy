from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from itertools import chain


class MyApp(App):
    def build(self):
        self.alphabet = [chr(i) for i in chain(range(1040, 1046), range(1025, 1026), range(1046, 1069),range(32, 33),range(1069, 1072))]
        gr = GridLayout(cols=5, padding=[35], spacing=3)
        for i in self.alphabet:
            gr.add_widget(Button(text=i, on_press=self.button_press))
        return gr

    def button_press(self, instance):
        print(instance.text)


if __name__ == '__main__':
    MyApp().run()
