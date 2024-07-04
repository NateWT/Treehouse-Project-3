from phrase import Phrase
import random
import sys

class Game():
    def __init__(self):
        self.guesses = [" "]
        self.missed = 0
        self.phrases = [
            Phrase("A piece of cake"),
            Phrase("Costs an arm and a leg"),
            Phrase("By the skin of your teeth"),
            Phrase("A bad apple"),
            Phrase("As right as rain")
        ]
        self.reset_game()

    def reset_game(self):
        self.guesses = [" "]
        self.missed = 0
        self.active_phrase = self.get_random_phrase()

    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print('     ===========================================')
        print('     Test how well you know the English language')
        print('     ===========================================')

    def get_guesses(self):
        while True:
            user_guess = input('\nEnter a letter: ').lower()
            if len(user_guess) == 1 and user_guess.isalpha():
                return user_guess
            else:
                print('You can only enter only 1 character and it must be a letter')
                continue

    def game_over(self):
        if self.missed == 5:
            print("It seems you could use a little work on your English, Sorry.")
        else:
            self.active_phrase.display(self.guesses)
            print("\nCongratulations, it seems like you know the English language.")
        
        restart = input("Would you be interested in trying agian?\n(Yes/No)")
        if restart == "Yes":
            self.reset_game()
            self.start()
        elif restart == "No":
            sys.exit()
        else:
            print("Just enter a Yes or a No please.")

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f'Number missed: {self.missed}')
            self.active_phrase.display(self.guesses)
            user_guesses = self.get_guesses()
            self.guesses.append(user_guesses)
            if not self.active_phrase.check_letter(user_guesses):
                self.missed += 1
        self.game_over()