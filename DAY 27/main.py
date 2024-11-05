from cProfile import label
from tkinter import *


def on_click_calculate():
    value=input.get()
    result= float(value) * 1.609344
    label2.config(text=f'{round(result,2)} Km')


window=Tk()
window.title("Miles to KM Converter")
window.minsize(width=500,height=500)
window.config(background="white",padx=20,pady=20)

headings=Label(text="Miles to KM convertor")
headings.config(background="white",font=('Ariel',14,'bold'),padx=20,pady=20)
headings.grid(column=2,row=0)



labels=Label(text="Miles : ")
labels.grid(column=2,row=1)


input = Entry()
input.config(width=3)
input.grid(column=3,row=1)


labels=Label(text="KM : ")
labels.grid(column=2,row=2)

label2=Label(text="0")
label2.grid(column=3,row=2)


button=Button(text="Calculate",command=on_click_calculate)
button.grid(column=2,row=6)

window.mainloop()


