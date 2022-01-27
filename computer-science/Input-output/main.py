#!/usr/bin/env python3

from src import number

number = number(0, 5)

numberGuess = input("Guess a number between 0 and 5: ")

if int(numberGuess) > 5:
    print("Number can't be greater than 5")
    exit()

if (numberGuess == number):
    print("You guessed the number!")
else:
    print("You didn't guess the number!")
    print(f"The number was {number}")
