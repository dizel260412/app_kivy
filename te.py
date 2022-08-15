from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from itertools import chain
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


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
        self.manager.current = 'secondscreen'
        return instance.text


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text = ScreenMain.button_press  # Передаю переменную из button_press

        layout = GridLayout(cols=5, rows=5, padding=[35], spacing=10)
        layout.add_widget(Button(text=str(self.text), on_press=self._on_press_button_new_layout))
        # for i in range(1, 26):
        #     layout.add_widget(
        #         Button(
        #             text=f"{i}",
        #             background_color=[2, 1.5, 3, 1],
        #             size_hint=[1, 0.1],
        #             on_press=self._on_press_button_new_layout,
        #         )
        #     )
        self.add_widget(layout)

    def _on_press_button_new_layout(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'thirdscreen'


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=5, rows=5, padding=[35], spacing=10)
        layout.add_widget(Button(text='Hello', on_press=self._on_press_button_layout))
        self.add_widget(layout)

    def _on_press_button_layout(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'
        # self.form = Form()
        # self.form.start()
        # return self.form


# class Cell(Widget):
#     def __init__(self, x, y, size):
#         super().__init__()
#         self.size = (size, size)
#         self.pos = (x, y)
#
#
# class Form(Widget):
#     def __init__(self):
#         super().__init__()
#         self.cell = Cell(100, 100, 30)
#         self.add_widget(self.cell)
#
#     def start(self):
#         Clock.schedule_interval(self.update, 0.01)
#
#     def update(self, _):
#         self.cell.pos = (self.cell.pos[0] + 2, self.cell.pos[1] + 3)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(SecondScreen(name='secondscreen'))
        sm.add_widget(ThirdScreen(name='thirdscreen'))

        return sm


if __name__ == '__main__':
    MyApp().run()
