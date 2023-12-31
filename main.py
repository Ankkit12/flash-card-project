from tkinter import *
import pandas as pd
import random as rd
BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}


try:
    data = pd.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/spanish to english.csv")
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')

random_word = {}

def flash_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = rd.choice(data_dict)
    random_text_spanish = random_word["Spanish"]
    canvas.itemconfig(spanish_text, text="Spanish", fill="black")
    canvas.itemconfig(english_text, text=f"{random_text_spanish}", fill="black")
    canvas.itemconfig(can_img, image=card_front)
    flip_timer = window.after(3000, turn_card)


def turn_card():
    translate_english = random_word["English"]
    canvas.itemconfig(can_img, image=card_back)
    canvas.itemconfig(spanish_text, text="English", fill="white")
    canvas.itemconfig(english_text, text=f"{translate_english}", fill="white")


def save_progress():
    data_dict.remove(random_word)
    data1 = pd.DataFrame(data_dict)
    data1.to_csv("data/Words_to_learn.csv", index=False)
    flash_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, turn_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
can_img = canvas.create_image(400, 256, image=card_front)
spanish_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
english_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


image2_tick = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=image2_tick, highlightthickness=0, command=flash_card)
wrong_button.grid(row=1, column=0)

image1_tick = PhotoImage(file="images/right.png")
tick_button = Button(image=image1_tick, highlightthickness=0, command=save_progress)

tick_button.grid(row=1, column=1)

flash_card()

window.mainloop()






