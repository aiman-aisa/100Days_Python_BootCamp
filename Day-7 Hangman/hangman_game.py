from hangman_art import *
from hangman_words import *
import random

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in chosen_word:
    display.append("_")

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    
    # check if letter already guessed
    if guess in display:
        print("You've already guessed "+ guess)

    #Check guessed letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # reduce 'lives' by 1 if wrong guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        #print(lives)

    print(f"{' '.join(display)}")
    
    # print the ASCII art from stages
    print(stages[lives])

if lives == 0:
    print("You lose")
else:
    print("You win!")

