from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window

aaaa = 1
bbb=1

sm = ScreenManager()


class SuccApp(App):
    def __init__(self, **kvargs):
        super(SuccApp, self).__init__(**kvargs)

    def build(self):
        return sm


class FirstSuccScreen(Screen):
    def __init__(self, **kw):
        super(FirstSuccScreen, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        global bbb
        self.layout = GridLayout(cols=bbb)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

        for i in range(aaaa):
            btn = Button(text="succ", on_press=lambda x: succ())
            self.layout.add_widget(btn)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана
        self.layout.clear_widgets()  # очищаем список


class SuccScreen(Screen):
    def __init__(self, **kw):
        super(SuccScreen, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        global bbb
        self.layout = GridLayout(cols=bbb)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

        for i in range(aaaa):
            btn = Button(text="succ", on_press=lambda x: succc())
            self.layout.add_widget(btn)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана
        self.layout.clear_widgets()  # очищаем список


def succ():
    global aaaa, bbb
    aaaa = aaaa + 1
    if aaaa%12==0:
        bbb=bbb+1
    sm.add_widget(SuccScreen(name=str(aaaa)))
    set_screen(str(aaaa))
    # print(aaaa)

def succc():
    global aaaa, bbb
    aaaa = aaaa + 1
    if aaaa%12==0:
        bbb=bbb+1
    sm.add_widget(FirstSuccScreen(name=str(aaaa)))
    set_screen(str(aaaa))
    # print(aaaa)

def set_screen(name_screen):
    sm.current = name_screen


sm.add_widget(FirstSuccScreen(name='first'))
sm.add_widget(SuccScreen(name='second'))
if __name__ == '__main__':
    SuccApp().run()
