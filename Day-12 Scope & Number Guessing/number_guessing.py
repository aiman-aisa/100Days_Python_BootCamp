#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
import os

def check_guess(guess, number):
    if not guess.isnumeric():
        print("Wrong input")
        return False
    elif int(guess) < number:
        print("Too low.")
        return False
    elif int(guess) > number:
        print("Too high.")
        return False
    elif int(guess) == number:
        print(f"You got it! The answer was {number}.")
        return True 

def play_guess_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    #print(f"Pssst, the correct number is {number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': " )
    while difficulty.lower() not in ["easy", "hard"]:
        difficulty = input("Wrong Input. Please choose a difficulty. Type 'easy' or 'hard': " )
    if difficulty.lower() == 'easy':
        num_chance = 10
    elif difficulty.lower() == 'hard':
        num_chance = 5

    print(num_chance)
    guess = 0
    guess_finished = False
    while not guess_finished:
        print(f"You have {num_chance} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        #print(guess, type(guess))
        num_chance -= 1
        if check_guess(guess, number) or num_chance == 0:
            guess_finished = True
        else:
            print("Guess again.")
        


    if num_chance == 0:
        print("You've run out of guesses, you lose.")
        
play_guess_number()
play_again = True
while play_again:
    cont_play = input("Do you want to play again? Type 'y' or 'n': ")
    if cont_play == 'y':
        os.system("cls")
        play_guess_number()
    else:
        play_again = False
        print("Thank you for playing the Guessing Number!")
    
