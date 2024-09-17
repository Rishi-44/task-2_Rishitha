#Number Guessing Game using PYTHON
import random

starting_num = 1 
ending_num = 100
answer = random.randint(starting_num,ending_num)
guesses = 0 
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {starting_num} and {ending_num}")

while is_running:
    guess = input("Enter your Guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1 
        if guess < starting_num or guess > ending_num:
            print("That number is out of range")
            print(f"Please select a number between {starting_num} and {ending_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too High! Try again")
        else:
            print(f"CORRECT!The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {starting_num} and {ending_num}")
