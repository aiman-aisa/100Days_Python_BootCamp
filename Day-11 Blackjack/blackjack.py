############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

from art import logo
import random
import os

def deal_card(card_list, cards):
    card_list.append(cards[random.randint(0, len(cards) - 1)])
    
def calculate_score(card_list):
    total_card = sum(card_list)
    if total_card == 21:
        return 0
    elif 11 in card_list and total_card > 21:
        card_list.remove(11)
        card_list.append(1)
        calculate_score(card_list)
        return total_card
    return total_card

def check_blackJack(computer_score, user_score):
    if computer_score == 0:
        return True
    elif user_score == 0:
        return True
    elif user_score > 21:
        return True
    else:
        return False
    
def compare(computer_score, user_score):
    if computer_score == 0:
        print("Your opponent got a BlackJack, You Lose!")
    elif user_score == 0:
        print("You got a BlackJack. You win!")
    elif user_score == computer_score:
        print("Draw!!!")
    elif user_score > 21:
        print("You went over. You lose :(")
    elif computer_score > 21:
        print("Your opponent went over. You win!")
    elif computer_score > user_score:
        print("You Lose!")
    else:
        print("You win!")


def play_blackJack():
    game_finished = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)

    user_cards = []
    computer_cards = []
    for _ in range(0, 2):
        deal_card(user_cards, cards)
        deal_card(computer_cards, cards)    
        
    #user_cards = [11, 5]
    #computer_cards = [11, 10]

    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    if check_blackJack(computer_score, user_score):
        game_finished = True

        
    while not game_finished:
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        deal_again = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal_again == 'y':
            deal_card(user_cards, cards)
            user_score = calculate_score(user_cards)
            if check_blackJack(computer_score, user_score):
                game_finished = True
        else:
            game_finished = True         
                
    while computer_score < 17 and computer_score != 0 and user_score < 21:
        deal_card(computer_cards, cards)
        computer_score = calculate_score(computer_cards)        

    print(f"  Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"  Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    compare(computer_score, user_score)

play_again = True
play_blackJack()
while play_again:
    cont_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if cont_play == 'y':
        os.system("cls")
        play_blackJack()
    else:
        play_again = False
        print("Thank you for playing BlackJack!")
    

        