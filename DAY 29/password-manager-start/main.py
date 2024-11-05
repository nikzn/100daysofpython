from tkinter import *
from tkinter import messagebox
import json
import random
import pyperclip

BACKGROUND_COLOR="#DFF2EB"
PRIMARY_COLOR="#B9E5E8"
SECONDARY_COLOR="#7AB2D3"
TERTIARY_COLOR="#4A628A"
FONT="Courier"


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '|', '\\', '`', '~']

#----------------------------SEARCH GENAERATOR------------------------------#

def on_click_search():
        website = website_input.get()
        try:
            with open("password.json", "r") as data_file:
                password_data = json.load(data_file)
                print(password_data)
        except FileNotFoundError:
                messagebox.showerror(title="No data found",message="No Data Found")
        else:
            if website in password_data:
                email=password_data[website]["email"],
                password=password_data[website]["password"]
                messagebox.showinfo(title=f"{website} Password",message=f"Email:{email}, password:{password}")
            else:
                messagebox.showerror(title="No data found", message=f"No Data Found {website}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    random_letter=random.randint(8,10)
    random_number = random.randint(2,4)
    random_symbol = random.randint( 2,4)
    password_list=[]

    password_letter=[random.choice(letters) for _ in range(random_letter)]
    password_number = [str(random.choice(numbers)) for _ in range(random_number)]
    password_symbol = [random.choice(symbol) for _ in range(random_symbol)]

    password_list=password_letter+password_symbol+password_number

    random.shuffle(password_list)

    password="".join(password_list)
    pyperclip.copy(password)



    print(password)
    password_input.insert(0,string=password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_click_submit():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="Missing fields",message="Missing fields are there")
    else:
        try:
            with open("password.json", "r") as data_file:
                password_data = json.load(data_file)
        except FileNotFoundError:
            with open("password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            password_data.update(new_data)
            with open("password.json", "w") as data_file:
                json.dump(password_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.minsize(width=500,height=500)
window.title("Password Generator")
window.config(padx=20,pady=20,background=BACKGROUND_COLOR)


heading=Label(text="PASSWORD MANAGER",background=BACKGROUND_COLOR,fg=TERTIARY_COLOR,font=(FONT,20,"bold"))
heading.grid(row=0,column=1)


logo=Canvas(width=200,height=200,background=BACKGROUND_COLOR,highlightthickness=0)
password_logo=PhotoImage(file="logo.png")
logo.create_image(100,100,image=password_logo)
logo.grid(row=1,column=1)


website_label=Label(text="Website:",background=BACKGROUND_COLOR,fg=SECONDARY_COLOR,font=(FONT,12,"bold"))
website_label.grid(row=2,column=0)

website_input=Entry(width=32)
website_input.config(highlightthickness=0)
website_input.grid(row=2,column=1)


submit_button=Button(text="Search",command=on_click_search)
submit_button.config(background=TERTIARY_COLOR,highlightthickness=0)
submit_button.grid(row=2,column=2)


email_label=Label(text="Email:",background=BACKGROUND_COLOR,fg=SECONDARY_COLOR,font=(FONT,12,"bold"))
email_label.grid(row=3,column=0)

email_input=Entry(width=52)
email_input.config(highlightthickness=0)
email_input.insert(0,'nikhil@email.com')
email_input.grid(row=3,column=1,columnspan=2)


password_label=Label(text="Password:",background=BACKGROUND_COLOR,fg=SECONDARY_COLOR,font=(FONT,12,"bold"))
password_label.grid(row=4,column=0)

password_input=Entry(width=32)
password_input.config(highlightthickness=0)
password_input.grid(row=4,column=1)

generate_password_button=Button(text="Generate Password",command=generate_random_password)
generate_password_button.config(background=TERTIARY_COLOR,highlightthickness=0)
generate_password_button.grid(row=4,column=2)

submit_button=Button(text="Submit",command=on_click_submit,width=50)
submit_button.config(background=TERTIARY_COLOR,highlightthickness=0)
submit_button.grid(row=5,column=1,columnspan=2)












window.mainloop()
