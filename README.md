# Number Guessing Game - Python Internship Task 3

## Project Description
A command-line Python game where the computer randomly selects a number
between 1 and 100 and the player tries to guess it.

The program gives "Too high" or "Too low" hints, counts attempts, handles
invalid input, and allows the player to play another round.

## Internship Requirements Covered
- Random number generation using the `random` module.
- User guesses and input handling.
- Too high / too low hints.
- Attempt counting.
- `try/except` for invalid input.
- Range checking from 1 to 100.
- Replay option.
- Comments explaining the code.

## How to Run

Make sure Python 3.x is installed, then run:

```bash
python main.py
```

## Example

```text
Welcome to the Number Guessing Game!

========================================
       NUMBER GUESSING GAME
========================================
I have selected a number between 1 and 100.
Try to guess it!
Enter your guess: 30
Too low! Try again.
Enter your guess: 70
Too high! Try again.
Enter your guess: 55
Congratulations! You guessed the number!
The number was 55.
You guessed it in 3 attempt(s).

Do you want to play again? (y/n): n

Thanks for playing! Goodbye.
```

## Project Structure

```text
number_guessing_game_internship/
├── main.py
├── README.md
└── SUBMISSION_NOTES.md
```
