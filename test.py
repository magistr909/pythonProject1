import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import data
import random


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text='Слово'))

        self.insideofinside = GridLayout()
        self.insideofinside.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 4
        self.insideofinside.add_widget(self.inside)

        self.choice1 = ToggleButton(text="Вариант №1", group='choices')
        self.inside.add_widget(self.choice1)
        self.choice2 = ToggleButton(text="Вариант №2", group='choices')
        self.inside.add_widget(self.choice2)
        self.choice3 = ToggleButton(text="Вариант №3", group='choices')
        self.inside.add_widget(self.choice3)
        self.choice4 = ToggleButton(text="Вариант №4", group='choices')
        self.inside.add_widget(self.choice4)

        self.inside1 = GridLayout()
        self.inside1.cols = 2

        self.result = Label(text='true/false')
        self.inside1.add_widget(self.result)
        self.result1 = Label(text='123-123')
        self.inside1.add_widget(self.result1)
        self.insideofinside.add_widget(self.inside1)
        self.add_widget(self.insideofinside)

        self.submit = Button(text="Submit", font_size=40)
        self.insideofinside.add_widget(self.submit)



class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()