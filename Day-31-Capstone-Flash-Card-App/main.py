from tkinter import *
import pandas as pd
from random import choice
import timer

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ---------------------------- NEXT CARD, FLIP CARD ------------------------------- #
try:
    words_df = pd.read_csv(r"Day-31-Capstone-Flash-Card-App\data\words_to_learn.csv")
except FileNotFoundError:
    words_df = pd.read_csv(r"Day-31-Capstone-Flash-Card-App\data\french_words.csv")
words_dict = words_df.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_dict)
    canvas.itemconfig(title_text, text="French", fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    #print(len(words_dict))

def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card['English'], fill="white") 
    
# ---------------------------- SAVE WORD FILE ------------------------------- #
def known():
    words_dict.remove(current_card)
    new_data = pd.DataFrame(words_dict)
    new_data.to_csv(r"Day-31-Capstone-Flash-Card-App\data\words_to_learn.csv", index=False)
    next_card()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Flash Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=r"Day-31-Capstone-Flash-Card-App\images\card_front.png")
card_back_img = PhotoImage(file=r"Day-31-Capstone-Flash-Card-App\images\card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file=r"Day-31-Capstone-Flash-Card-App\images\right.png")
wrong_img = PhotoImage(file=r"Day-31-Capstone-Flash-Card-App\images\wrong.png")
right_button = Button(image=right_img, highlightthickness=0, command=known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

