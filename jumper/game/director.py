from game.terminal_service import TerminalService
from game.graphic import Graphic
from game.word import Word

class Director:
    def __init__(self):
        self._word = Word()
        self._graphic = Graphic()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.guessed_word = ""
        self.lives = 5
        self.wordToGuess = []
        
    def start_game(self):
        self.guessed_word = self._word.new_word()
        self._wordToGuess = self._word.letters
        self._word.print_blanks() 
        self._graphic.print_parachute(self.lives)
        while self._is_playing:
            guess = self._get_inputs()
            self._do_updates(guess)
            self._do_outputs()

    def _get_inputs(self):
        guess_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        return guess_letter

    def _do_updates(self, guess):
        wrong_letter = []
        found_letter = False
        chosen_word = []

        for letter in self.guessed_word:
            chosen_word.append(letter)

        for i in range(0, len(chosen_word)):
            letter = chosen_word[i]
            if guess == letter:
                self._word.letters[i] = letter
                found_letter = True

        if found_letter == False:
            self.lives -= 1
            wrong_letter.append(guess)
            self._terminal_service.write_text(wrong_letter)

        self._word.print_blanks()
        self._graphic.print_parachute(self.lives)
            

    def _do_outputs(self):
        if self.lives == 0:
            self._is_playing = False
        
        if "_" not in self._word.letters:
            self._is_playing = False
