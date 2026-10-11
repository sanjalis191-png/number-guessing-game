"""
Number Guessing Game - Python Internship Task 3
"""

import random


def play_game():
    """Run one round of the number guessing game."""
    # Generate a random number between 1 and 100.
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n" + "=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            # Get the player's guess.
            guess = int(input("Enter your guess: "))

            # Check that the guess is in the allowed range.
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Count valid guesses.
            attempts += 1

            # Compare the guess with the secret number.
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("\nCongratulations! You guessed the number!")
                print(f"The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempt(s).")
                break

        except ValueError:
            # Handle input that is not a whole number.
            print("Invalid input. Please enter a whole number.")


def main():
    """Start the game and allow multiple rounds."""
    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()

        # Ask whether the player wants another round.
        while True:
            again = input("\nDo you want to play again? (y/n): ").strip().lower()

            if again in ("y", "yes"):
                break
            elif again in ("n", "no"):
                print("\nThanks for playing! Goodbye.")
                return
            else:
                print("Please enter y for yes or n for no.")


if __name__ == "__main__":
    main()
