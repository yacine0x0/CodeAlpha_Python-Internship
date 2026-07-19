import random

import pyfiglet

print(pyfiglet.figlet_format("HANGMAN  GAME"))


words = ["fruit", "bike", "river", "basketball", "cinema"]
random_word = random.choice(words).lower()
guess = ["_"] * len(random_word)
attempts = 6
guessed_letters = set()

while attempts > 0:
    if random_word == "".join(guess):
        break

    print(" ".join(guess))
    print(f"Attempts remaining: {attempts}")
    try:
        letter_guessed = input("Guess a letter: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        exit()

    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        print("Invalid input. Enter a single letter a-z.\n")
        continue

    if letter_guessed in guessed_letters:
        print(f"You already guessed '{letter_guessed}'. Try a different letter.\n")
        continue

    guessed_letters.add(letter_guessed)

    if letter_guessed in random_word:
        for i, letter in enumerate(random_word):
            if letter == letter_guessed:
                guess[i] = letter_guessed
    else:
        attempts -= 1
        print(f"'{letter_guessed}' is not in the word.\n")

if attempts > 0:
    print(f"You guessed it! The word was '{random_word}'.")
else:
    print(f"You lost. The word was '{random_word}'.")
