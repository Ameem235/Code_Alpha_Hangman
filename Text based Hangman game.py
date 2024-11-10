import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "computer", "developer"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    guessed = ''
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    
    while tries > 0:
        print(display_hangman(tries))
        print("Word: ", ' '.join([letter if letter in guessed else '_' for letter in word]))
        print("Guessed letters: ", ' '.join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            guessed += guess
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

        if all(letter in guessed for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(display_hangman(tries))
        print(f"Sorry, you've run out of tries. The word was: {word}")

if __name__ == "__main__":
    hangman()