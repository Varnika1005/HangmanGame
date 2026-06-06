
# Hangman game

import random

def hangman_game():
    print("\nWelcome to Hangman!")
    while True:
        # List of possible words
        word_list = ["apple", "brain", "chess", "daisy", "eagle"]
        # Choosing a random word from the list
        word = random.choice(word_list)
        guessed = []
        wrong_guesses = 0
        max_attempts = 6

        # Display with underscores for unguessed letters
        display = ["_" for _ in word]
        print("\nLet's start! You have", max_attempts, "wrong guesses allowed.")

        while wrong_guesses < max_attempts and "_" in display:
            print("\nWord:", " ".join(display))
            guess = input("Enter a letter: ").lower()

            # Check for valid single letter input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed:
                print("You already tried that letter.")
                continue

            guessed.append(guess)

            if guess in word:
                print("Nice guess!")
                for i in range(len(word)):
                    if word[i] == guess:
                        display[i] = guess
            else:
                wrong_guesses += 1
                print("Oops! That letter’s not in the word.")
                print("Tries left:", max_attempts - wrong_guesses)

        # End of game round
        if "_" not in display:
            print("\nYou got it! The word was:", word)
        else:
            print("\nGame over. The word was:", word)

        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing. See you next time!")
            break

# Call the function to start the game
hangman_game()
