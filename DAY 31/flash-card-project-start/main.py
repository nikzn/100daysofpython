from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
RANDOM_DATA={}
dict_french={}

try:
    french_dictionary=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError :
    french_dictionary = pandas.read_csv("./data/french_words.csv")
    dict_french = french_dictionary.to_dict(orient="records")
else:
    dict_french = french_dictionary.to_dict(orient="records")







def next_card():
    global RANDOM_DATA,flip_timer
    RANDOM_DATA = random.choice(dict_french)
    print(RANDOM_DATA)
    random_french=RANDOM_DATA['French']
    card.itemconfig(card_word,text="French",fill="black")
    card.itemconfig(card_texts,text=random_french,fill="black")
    card.itemconfig(card_image,image=card_front_img)
    flip_timer=window.after(3000,func=flip_slider)

def flip_slider():
    global RANDOM_DATA
    random_english=RANDOM_DATA['English']
    card.itemconfig(card_image,image=card_back_img)
    card.itemconfig(card_word, text="English",fill="white")
    card.itemconfig(card_texts, text=random_english,fill="white")


def is_known():
    dict_french.remove(RANDOM_DATA)
    known_french = pandas.DataFrame(dict_french)
    known_french.to_csv(path_or_buf="./data/words_to_learn.csv",index=False)
    next_card()

window=Tk()
window.minsize(width=500,height=500)
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Capstone")

card=Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file="./images/card_front.png")
card_back_img=PhotoImage(file="./images/card_back.png")
card_image=card.create_image(400,263,image=card_front_img)
card_word=card.create_text(400,150,text="",font=('Ariel',40,'italic'))
card_texts=card.create_text(400,263,text="",font=('Ariel',60,'bold'))
card.grid(row=0,column=0,columnspan=2)



cross_img=PhotoImage(file='./images/wrong.png')
cross=Button(image=cross_img,highlightthickness=0,command=next_card)
cross.grid(row=1,column=0)



tick_img=PhotoImage(file='./images/right.png')
tick=Button(image=tick_img,highlightthickness=0,command=is_known)
tick.grid(row=1,column=1)


next_card()

flip_timer=window.after(3000,func=flip_slider)

window.mainloop()
