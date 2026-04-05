from tkinter import *
#---------------------------------PASSWORD GENERATOR----------------------------------------------------#


#-----------------------------SAVE PASSWORD--------------------------------------------------------------#
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    print("Save clicked:", website, username, password) 
    with open("C:\\Users\\Preksha Asati\\PY\\Day 29\\password_manager.txt", "a") as f:
        f.write(website +" | " + username + " | " + password + "\n\n")

#----------------------------------UI SETUP --------------------------------------------------------------#

window= Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas= Canvas(width=200,height=200)
password_img= PhotoImage(file="C:\\Users\\Preksha Asati\\PY\\Day 29\\password_img.png")
canvas.create_image(100,100,image=password_img)
#canvas.config(padx=20,pady=20)
canvas.grid(column=1,row=0)
#columnspan -->of grid -->to spead a element in how many columns of the grid 

website_lbl= Label(text="Website")
website_lbl.grid(column=0,row=1)

website_entry = Entry(width=53,highlightthickness=0)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()#focus curson in the entry


username_lbl= Label(text="Email/Username")
username_lbl.grid(column=0,row=2)

username_entry = Entry(width=53,highlightthickness=0)
username_entry.grid(column=1,row=2,columnspan=2)
#pre-populating an email entry 
username_entry.insert(0,"prekshaasat02@gmail.com")

password_lbl= Label(text="Password")
password_lbl.grid(column=0,row=3)

password_entry = Entry(width=32 ,highlightthickness=0 )
password_entry.grid(column=1,row=3)

password_button = Button(text="Generate Password",highlightthickness=0,width=15)
password_button.grid(column=2,row=3,columnspan=1)

Add_button = Button(text="Add",width=51,padx=0,pady=0,highlightthickness=0,command=save)
Add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()
