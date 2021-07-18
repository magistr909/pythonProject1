import kivy
from functools import partial
import data
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.uix.pagelayout import PageLayout
from translate import Translator
import random

global type_of_match_the_words


Builder.load_string("""
<StartScreen>:
    GridLayout:
        cols: 1
        Button:
            text: "Match the Words"
            font_name: "Droid"
            background_color : 
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0.5
                root.manager.current = 'Match the words type'
        Button:
            text: "Search in data base"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0.5
                root.manager.current = 'Search'
        Button:
            text: "Add to data base"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0.5
                root.manager.current = 'AddDB'
        Button:
            text: "Common mistakes"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0.5
                root.manager.current = 'Body'
                app.word_list = app.type_check("6") 
                app.typus = '6'

<MatchTheWordsType>:
    GridLayout:
        cols: 1
        Button:
            text: "汉语 → Russian"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Body'
                app.word_list = app.type_check("1")
                app.typus = '1'
        Button:
            text: "汉语 → Transcription"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Body'
                app.word_list = app.type_check("2")
                app.typus = '2'
        Button:
            text: "Russian → 汉语"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Body'
                app.word_list = app.type_check("3")
                app.typus = '3'
        Button:
            text: "Transcription → 汉语"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Body'
                app.word_list = app.type_check("4")
                app.typus = '4'
        Button:
            text: "Random"
            font_name: "Droid"
            background_color : 
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'Body'
                app.word_list = app.type_check("5") 
                app.typus = '5'
                print(app.word_list)    
        

<BodyMatchTheWords>:
    GridLayout:
        cols: 1
        Label:
            text: app.word_list[0][1]
            font_name: "Droid"
        GridLayout:
            cols: 2
            ToggleButton:
                id: tb1
                text: app.word_list[1][0]
                font_name: "Droid"
                group: 'choices'
                on_press: root.current_value = 0
            ToggleButton:
                id: tb2
                text: app.word_list[1][1]
                font_name: "Droid"
                group: 'choices'
                on_press: root.current_value = 1
            ToggleButton:
                id: tb3
                text: app.word_list[1][2]
                font_name: "Droid"
                group: 'choices'
                on_press: root.current_value = 2
            ToggleButton:
                id: tb4
                text: app.word_list[1][3]
                font_name: "Droid"
                group: 'choices'
                on_press: root.current_value = 3
        Button:
            text: "Check"
            font_name: "Droid"
            background_color: 
            on_press:                
                if app.typus != '6': root.check_answer(app.word_list[0][0], app.word_list[1], app.word_list[2], 'normal')
                if app.typus != '6': app.word_list = app.type_check(app.typus)
                else: root.check_answer(app.word_list[0][0], app.word_list[1], app.word_list[2], 'karma')
        GridLayout:
            cols: 2
            Label:
                text: str(root.status)
                font_name: "Droid"
            Label:
                text: str(root.right_answer)
                font_name: "Droid"

<SearchInDataBase>
    PageLayout:
        GridLayout:
            cols: 1
            Label:
                text: ''
                font_name: "Droid"
            TextInput:
                id: searchinput
                font_name: "Droid"
            Button
                text: 'Search'
                font_name: "Droid"
                on_press:
                    root.search_in_database()
        GridLayout:
            cols: 1
            Label:
                id: searchoutput
                text: 'Found data'
                font_name: "Droid"
                background_color: (0, 0, 0, 1)
                canvas.before:
                    Color:
                        rgba: self.background_color
                    Rectangle:
                        size: self.size
                        pos: self.pos

<AddToDataBase>
    GridLayout:
        cols:1
        GridLayout:
            cols:2
            Label:
                text: 'Hanzi'
                font_name: "Droid"
            TextInput:
                id: s1
                multiline: False
                font_name: "Droid"
            Label:
                text: 'Transcription'
                font_name: "Droid"
            TextInput:
                id: s2
                multiline: False
                font_name: "Droid"
            Label:
                text: 'Translation'
                font_name: "Droid"
            TextInput:
                id: s3
                multiline: False
                font_name: "Droid"
        GridLayout:
            cols: 1
            Button:
                text: 'Submit'
                font_name: "Droid"
                on_press: root.add_toDB()
""")

LabelBase.register(name="Droid",
                   fn_regular="DroidSansFallback.ttf")


class StartScreen(Screen):
    pass

class MatchTheWordsType(Screen):
    pass


class BodyMatchTheWords(Screen):
    right_answer = ObjectProperty()
    status = ObjectProperty()
    current_value = NumericProperty()
    def __init__(self, **kwargs):
        super(BodyMatchTheWords, self).__init__(**kwargs)
        self.right_answer = '123'
        self.status = 'check'
        self.current_value = 5
    def check_answer(self, answer, select_list, right_answer, mode):
        num = int(self.current_value)
        if select_list[num] == answer:
            print(True)
            self.status = 'True'
            self.right_answer = f'{right_answer[0]} - {right_answer[1]} - {right_answer[2]}'
            if mode == 'karma':
                data.plus_karma([right_answer[0], right_answer[1], right_answer[2]])
        else:
            print(False)
            self.status = 'False'
            self.right_answer = f'{right_answer[0]} - {right_answer[1]} - {right_answer[2]}'
            if mode == 'normal':
                data.minus_karma([right_answer[0], right_answer[1], right_answer[2]])


class SearchInDataBase(Screen):
    current_value = NumericProperty()

    def __init__(self, **kwargs):
        super(SearchInDataBase, self).__init__(**kwargs)
        self.current_value = 5

    def search_in_database(self):
        text = self.ids.searchinput.text
        searchdata = data.search_in_database(text)
        sentence = ''
        for i in searchdata:
            sentence += " ".join(i)
            sentence += "\n"
        self.ids.searchoutput.text = sentence
        print(sentence)
        print(searchdata)



class AddToDataBase(Screen):
    def add_toDB(self):
        data.add_to_db(self.ids.s1.text, self.ids.s2.text, self.ids.s3.text)

class MyApp(App):
    word_list = ObjectProperty()
    typus = ObjectProperty()
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.word_list = self.type_check('5')
        self.typus = 'sus'

    def set_the_names(self):
        self.answer = self.type[0][0]
        self.keyword = self.type[0][1]
        self.choice1 = self.type[1][0]
        self.choice2 = self.type[1][1]
        self.choice3 = self.type[1][2]
        self.choice4 = self.type[1][3]
        self.correct_line = f"{self.type[2][0]}-{self.type[2][1]}-{self.type[2][2]}"

    def type_check(self, typecheck):
        if typecheck == "1":
            self.type = Translator().turn('1', 'normal')
            self.set_the_names()
        if typecheck == "2":
            self.type = Translator().turn('2', 'normal')
            self.set_the_names()
        if typecheck == "3":
            self.type = Translator().turn('3', 'normal')
            self.set_the_names()
        if typecheck == "4":
            self.type = Translator().turn('4', 'normal')
            self.set_the_names()
        if typecheck == "5":
            self.type = Translator().turn('5', 'normal')
            self.set_the_names()
        if typecheck == "6":
            self.type = Translator().turn('5', 'karma')
            self.set_the_names()
        print(self.type)
        list_of_data = self.type
        return self.type

    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(StartScreen(name='Start'))
        self.screen_manager.add_widget(MatchTheWordsType(name='Match the words type'))
        self.screen_manager.add_widget(BodyMatchTheWords(name='Body'))
        self.screen_manager.add_widget(SearchInDataBase(name='Search'))
        self.screen_manager.add_widget(AddToDataBase(name='AddDB'))

        return self.screen_manager


if __name__ == "__main__":
    learn_language_app = MyApp()
    learn_language_app.run()
