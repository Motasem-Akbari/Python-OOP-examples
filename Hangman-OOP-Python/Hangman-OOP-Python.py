import random


class HangmanGame:
    def __init__(self):
        self.__word = random.choice(['python', 'banana', 'computer'])
        self.guesses = []
        self.__attempts = 6

    @property
    def attempts_left(self):
        return self.__attempts

    def make_guess(self, letter):
        if letter in self.guesses:
            print("You already guessed that letter.")
            return

        self.guesses.append(letter)
        print(f"Your guesses: {self.guesses}")

        if letter not in self.__word:
            self.__attempts -= 1
            print(f"Wrong guess! Attempts left: {self.__attempts}")
        else:
            print("Good guess!")

    def display_progress(self):
        progress = [
            letter if letter in self.guesses else '_' for letter in self.__word]
        print(' '.join(progress))
        return progress

    def is_won(self):
        return all(letter in self.guesses for letter in self.__word)

    @property
    def get_word(self):
        return self.__word


if __name__ == "__main__":
    game = HangmanGame()
    while game.attempts_left > 0:
        game.display_progress()
        letter = input("Enter a letter: ").lower()
        game.make_guess(letter)

        if game.is_won():
            print("\nYOU WON! :D")
            print(f"The word was: {game.get_word}")
            break
    else:
        print("\nYOU LOST T_T")
        print(f"The word was: {game.get_word}")
