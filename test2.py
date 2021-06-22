import kivy
from functools import partial
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import data
import random

class StartScreen(GridLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.cols = 1

        self.match_the_words_type_btn = Button(text="Match the Words")
        self.match_the_words_type_btn_partial = partial(self.select_screen, "Match the words type")
        self.match_the_words_type_btn.bind(on_press=self.match_the_words_type_btn_partial)
        self.search_in_db_btn = Button(text="Search in data base")
        self.add_to_data_base_btn = Button(text="Add to data base")
        self.common_mistakes_btn = Button(text="Common mistakes")
        self.settings_btn = Button(text="Settings")
        self.about_the_app_btn = Button(text="About the App")

        self.add_widget(self.match_the_words_type_btn)
        self.add_widget(self.search_in_db_btn)
        self.add_widget(self.add_to_data_base_btn)
        self.add_widget(self.common_mistakes_btn)
        self.add_widget(self.settings_btn)
        self.add_widget(self.about_the_app_btn)

    def select_screen(self, screen_name, instance):
        learn_language_app.screen_manager.current = f"{screen_name}"

class MatchTheWordsType(GridLayout):
    def __init__(self, **kwargs):
        super(MatchTheWordsType, self).__init__(**kwargs)
        self.cols = 1

        self.hanyu_to_russian_btn = Button(text="汉语 → Russian")
        self.hanyu_to_russian_partial = partial(self.select_screen,"Body match the words")
        self.hanyu_to_russian_btn.bind(on_press=self.hanyu_to_russian_partial)
        self.hanyu_to_transcription_btn = Button(text="汉语 → Transcription")
        self.hanyu_to_transcription_partial = partial(self.select_screen, "Body match the words")
        self.russian_to_hanyu_btn = Button(text="Russian → 汉语")
        self.hanyu_to_russian_partial = partial(self.select_screen, "Body match the words")
        self.transcription_to_hanyu_btn = Button(text="Transcription → 汉语")
        self.hanyu_to_russian_partial = partial(self.select_screen, "Body match the words")
        self.random_btn = Button(text="Random")
        self.hanyu_to_russian_partial = partial(self.select_screen, "Body match the words")

        self.add_widget(self.hanyu_to_russian_btn)
        self.add_widget(self.hanyu_to_transcription_btn)
        self.add_widget(self.russian_to_hanyu_btn)
        self.add_widget(self.transcription_to_hanyu_btn)
        self.add_widget(self.random_btn)

    def select_screen(self, screen_name, mode, instance):
        learn_language_app.screen_manager.current = f"{screen_name}"


class BodyMatchTheWords(GridLayout):
    def __init__(self, **kwargs):
        super(BodyMatchTheWords, self).__init__(**kwargs)
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
        self.screen_manager = ScreenManager()

        self.start_page = StartScreen()
        screen = Screen(name="Start")
        screen.add_widget(self.start_page)
        self.screen_manager.add_widget(screen)

        self.match_the_word_type_page = MatchTheWordsType()
        screen = Screen(name="Match the words type")
        screen.add_widget(self.match_the_word_type_page)
        self.screen_manager.add_widget(screen)

        self.body_match_the_word_type_page = BodyMatchTheWords()
        screen = Screen(name="Body match the words")
        screen.add_widget(self.body_match_the_word_type_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    learn_language_app = MyApp()
    learn_language_app.run()