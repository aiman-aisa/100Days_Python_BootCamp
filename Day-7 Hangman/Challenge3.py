#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in chosen_word:
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while "_" in display:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            print(f"Current position: {i}\n Current letter: {chosen_word[i]}\n Guessed letter: {guess}")
            display[i] = guess

    print(display)
print("You win!")