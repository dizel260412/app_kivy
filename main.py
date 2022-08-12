from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from itertools import chain
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenMain(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alphabet = [chr(i) for i in chain(range(1040, 1046), range(1025, 1026), range(1046, 1069), range(32, 33),
                                               range(1069, 1072))]
        gr = GridLayout(cols=5, padding=[35], spacing=3)
        for i in self.alphabet:
            gr.add_widget(Button(text=i, on_press=self.button_press))
        self.add_widget(gr)

    def button_press(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second_screen'
        print(instance.text)
        return instance.text


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        get = ScreenMain.button_press
        layout = GridLayout(cols=5, rows=5, padding=[35], spacing=10)
        layout.add_widget(Button(text=str(get)))
        # for i in range(1, 26):
        #     layout.add_widget(
        #         Button(
        #             text=f"{ScreenMain.button_press}",
        #             background_color=[2, 1.5, 3, 1],
        #             size_hint=[1, 0.1],
        #             on_press=self._on_press_button_new_layout,
        #         )
        #     )
        self.add_widget(layout)

    def _on_press_button_new_layout(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(SecondScreen(name='second_screen'))

        return sm


if __name__ == '__main__':
    MyApp().run()
