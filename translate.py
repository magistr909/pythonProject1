import data
import random

class Translator:
    def turn(self,type, mode):
        self.get_random_turn(mode)
        self.etalon_datalist = self.datalist[0]
        self.etalon_hanzi = self.hanzi
        self.etalon_transcription = self.transcription
        self.etalon_translation = self.translation
        self.this_turn_list = self.get_four_choices()
        self.checking_type_of_sort(type)
        return ((self.answer,
                 self.keyword), (self.choice1,
                                 self.choice2,
                                 self.choice3,
                                 self.choice4),(self.etalon_hanzi,
                                                self.etalon_transcription,
                                                self.etalon_translation))


    def answer_check(self,etalon):
        for i in [self.choice1, self.choice2, self.choice3, self.choice4]:
            if i == etalon:
                self.answer = i

    def checking_type_of_sort(self, type):
        if type == '1':
            self.keyword = self.etalon_hanzi
            self.matching_the_choices(3)
            self.answer_check(self.etalon_translation)
        if type == '2':
            self.keyword = self.etalon_hanzi
            self.matching_the_choices(2)
            self.answer_check(self.etalon_transcription)
        if type == '3':
            self.keyword = self.etalon_translation
            self.matching_the_choices(1)
            self.answer_check(self.etalon_hanzi)
        if type == '4':
            self.keyword = self.etalon_transcription
            self.matching_the_choices(1)
            self.answer_check(self.etalon_hanzi)
        if type == '5':
           self.checking_type_of_sort(random.choice(['1','2','3','4']))

    def matching_the_choices(self, index):
        self.choice1 = self.this_turn_list[0][index]
        self.choice2 = self.this_turn_list[1][index]
        self.choice3 = self.this_turn_list[2][index]
        self.choice4 = self.this_turn_list[3][index]

    def get_four_choices(self):
        self.choices = []
        self.choices.append(self.etalon_datalist)
        for i in range(1,4):
            self.choices.append(self.datalist[i])
        return random.sample(self.choices, len(self.choices))
    def get_random_turn(self,mode):
        self.datalist = self.randomize_data(mode)
        self.hanzi = self.datalist[0][1]
        self.transcription = self.datalist[0][2]
        self.translation = self.datalist[0][3]

    def randomize_data(self,mode):
        if mode == 'normal':
            self.wholedata = data.chalna_select_main()
        if mode == 'karma':
            self.wholedata = data.chalna_select_mistakes()
        return random.sample(self.wholedata, len(self.wholedata))


if __name__ == "__main__":
    print(Translator().turn('5', 'karma'))