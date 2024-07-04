class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def check_letter(self, letter):
        return letter.lower() in self.phrase

    def display(self, guesses):
        for letter in self.phrase:
            if letter.lower() in guesses:
                print(f'{letter}', end=' ')
            else:
                print("_", end=' ')

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter.isalpha() and letter.lower() not in guesses:
                return False
        return True