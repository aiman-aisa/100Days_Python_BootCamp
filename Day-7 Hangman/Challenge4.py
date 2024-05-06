# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in chosen_word:
    display.append("_")

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for i in range(len(chosen_word)):
        #print(f"Current position: {i}\n Current letter: {chosen_word[i]}\n Guessed letter: {guess}")
        if chosen_word[i] == guess:
            display[i] = guess
        
        # reduce 'lives' by 1 if wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(lives)

    print(f"{' '.join(display)}")
    
    # print the ASCII art from stages
    print(stages[lives])

if lives == 0:
    print("You lose")
else:
    print("You win!")