import random

class Word:

    def __init__(self):
        self._words = ['argentina','worldcup', 'champion']
        self._word = ""
        self.letters = []
 

    def new_word(self):
        self._word = random.choice(self._words)
        
        self.hide_word()
        return self._word

    def hide_word(self):
        self.letters = []
        for i in range(len(self._word)):
            self.letters.append("_")
        return self.letters

    def print_blanks(self):
        self.blanks = " ".join(self.letters)
        print(self.blanks) 