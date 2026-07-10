# Day 14 Notes - Number Guessing Game Project
# Project Overview
Today I built my first standalone Python project, **Number Guessing Game**.
The game generates a random number based on the selected difficulty level, and the player has to guess the correct number. After every guess, the program provides hints until the correct number is found.
This project combines multiple Python concepts learned over the past 13 days into one complete application.

# Project Objectives
Build an interactive console application.
Practice combining multiple Python concepts.
Improve problem-solving skills.
Create the first portfolio-ready project for GitHub.

# Concepts Used
### Variables
Variables were used to store:
Difficulty level
Maximum number
Secret random number
User's guess
Number of attempts
Example:
python id="k8m4hs"
maximum = 100
attempt = 0
### User Input
The `input()` function was used to:
Select the difficulty level
Enter guesses
Example:
python id="czzbln"
choice = input("Choose Difficulty (1/2/3): ")
### Conditional Statements
`if`, `elif`, and `else` were used to:
Select the difficulty level
Compare the guessed number with the secret number
Example:
python id="swl3m7"
if guess < secret:
    print("Too Low!")
elif guess > secret:
    print("Too High!")
else:
    print("Congratulations!")
### Loops
A `while True` loop keeps the game running until the player guesses the correct number.
Example:
python id="x8v6wc"
while True:
The loop ends using:
python id="4r6a4l"
break
### Random Module
The `random` module generates a random secret number.
Example:
python id="mjyx9n"
import random
secret = random.randint(1, maximum)
### Exception Handling
`try` and `except` prevent the program from crashing if the user enters invalid input.
Example:
python id="rkofgc"
try:
    guess = int(input("Enter your guess: "))
except ValueError:
    print("Please enter a valid number!")

# Algorithm
1. Display the game title.
2. Ask the player to choose a difficulty level.
3. Generate a random number based on the selected difficulty.
4. Initialize the attempt counter.
5. Ask the player to guess the number.
6. Handle invalid input using exception handling.
7. Compare the guess with the secret number.
8. Display "Too High!" or "Too Low!" if the guess is incorrect.
9. Display a success message and total attempts when the correct number is guessed.
10. End the game.

# Features Implemented
Difficulty selection
Random number generation
Unlimited guessing attempts
Hint system
Attempt counter
Exception handling
User-friendly console output

# Future Improvements
Add a "Play Again" option.
Allow the player to quit by entering `q`.
Add a timer to track how long the player takes.
Save the best score in a file.
Add a scoring system based on the number of attempts.
Use colored console output for a better user experience.

# Key Functions and Modules Used
`input()`
`print()`
`int()`
`random.randint()`
`try`
`except`
`while`
`break`