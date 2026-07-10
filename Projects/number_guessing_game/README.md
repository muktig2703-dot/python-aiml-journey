# Number Guessing Game

## Project Description
The **Number Guessing Game** is a simple Python console application where the computer randomly selects a number, and the player tries to guess it.
The game provides hints after each guess, telling the player whether the guess is **too high** or **too low** until the correct number is found.
Players can also choose from different difficulty levels, making the game more fun and challenging.

## Features
 Three difficulty levels:
  Easy (1–50)
  Medium (1–100)
  Hard (1–500)
Random number generation using Python's `random` module
Helpful hints ("Too High!" or "Too Low!")
Counts the number of attempts taken
Handles invalid input using exception handling
Displays a success message when the correct number is guessed

## Technologies Used
Python 3
Random Module
Exception Handling (`try` / `except`)
Loops
Conditional Statements

## Project Structure
text
Number_Guessing_Game/
│
├── main.py
└── README.md

## How to Run
1. Make sure Python 3 is installed.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the following command:
bash
python main.py

## Example Gameplay
text
Welcome to Number Guessing Game!
1. Easy (1-50)
2. Medium (1-100)
3. Hard (1-500)
Choose Difficulty (1/2/3): 2
Enter your Guess (1-100): 40
Too Low!
Enter your Guess (1-100): 80
Too High!
Enter your Guess (1-100): 65
Congratulations!
Attempts: 3

## Concepts Practiced
Variables
User Input
Conditional Statements
Loops
Random Module
Exception Handling
Program Logic

## Future Improvements
Play Again option
High Score Tracker
Save scores to a file
Timer to measure performance
Colored console output
Difficulty-based scoring system

## Author
**Mukti Gupta**
B.Tech – Artificial Intelligence & Machine Learning
Learning Python through a structured **30-Day Python for AI & ML Journey** while building projects and documenting progress on GitHub.