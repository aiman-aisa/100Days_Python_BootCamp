import random
from art import *
from game_data import data
import os

def pick_random(data):
    return data[random.randint(1, len(data) - 1)]

def compare(A, B):
    if A > B:
        return "a"
    else:
        return "b"

def game():
    score = 0
    game_end = False

    while not game_end:
        print(logo)
        A_dict = pick_random(data)
        B_dict = pick_random(data)
        
        print(f"Compare A: {A_dict['name']}, a {A_dict['description']}, from {A_dict['country']}.")
        print(f"Psst... A have {A_dict['follower_count']} followers")
        A_followers = A_dict['follower_count']
        print(vs)
        print(f"Against B: {B_dict['name']}, a {B_dict['description']}, from {B_dict['country']}.")
        print(f"Psst... B have {B_dict['follower_count']} followers")
        B_followers = B_dict['follower_count']
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if compare(A_followers, B_followers) == answer:
            score += 1
            print(score)
        else:
            game_end = True
        os.system("cls")
            
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    
game()
play_again = True
while play_again:
    cont_play = input("Do you want to play again? Type 'y' or 'n': ")
    if cont_play == 'y':
        os.system("cls")
        game()
    else:
        play_again = False
        print("Thank you for playing the Higher Lower!")
        