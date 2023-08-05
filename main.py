import pandas

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import time
import pandas as pd
import random
#-------------------------data reading--------------------------
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")

else:
    data_dict = df.to_dict(orient="records")
#-----------------------------loop-----------------------------
new_frenchword=""

def next_card():
    global new_frenchword,flip_time
    window.after_cancel(flip_time)
    new_frenchword = random.choice(data_dict)
    canvas.itemconfig(lang_text,text="French")
    canvas.itemconfig(word_text,text=new_frenchword["French"])
    canvas.itemconfig(images, image=frontimg)
    flip_time = window.after(3000,flip_card)








#------------------------------------------------------

# def show_english():
#     canvas.itemconfig(images, image=backimg)
#
#     canvas.itemconfig(word_text, text=english_word)
# score=1
# def show_french():
#     print("enter")
#     canvas.itemconfig(images,image=frontimg)
#     canvas.itemconfig(lang_text,text="French")
#
#
#     new_frenchword = random.choice(list(data_dict.keys()))
#     canvas.itemconfig(word_text,text=new_frenchword)
#     canvas.after(3000,show_english)





def flip_card():
    print("window after time", flip_time)

    canvas.itemconfig(lang_text, text="English")
    english_word = new_frenchword["English"]

    canvas.itemconfig(word_text,text=english_word)
    canvas.itemconfig(images, image=backimg)

def is_known():
    data_dict.remove(new_frenchword)
    print(len(data_dict))
    data=pd.DataFrame(data_dict)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()
#-----------------------------UI-----------------------------

window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.config(pady=50,padx=50)
# window.pack()
# print("window after time",flip_time)
frontimg = PhotoImage(file="./images/card_front.png")
backimg = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
images = canvas.create_image(400,263,image=frontimg)
lang_text = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
word_text = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

tick_image=PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image,command=is_known)
tick_button.grid(column=1,row=2)

wrong_image=PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,command=next_card)
wrong_button.grid(column=0,row=2)
# canvas.after(3000,show_french())
flip_time=window.after(3000,flip_card)

next_card()

window.mainloop()


