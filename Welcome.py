from tkinter import *
from PIL import *
import random

window = Tk()
window.geometry("500x350") #Resizing window
window.title("Quiz") #title
window.configure(bg = "white")
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)

lb1 = Label(window, text = "Quiz", bg = "white", fg = "black", borderwidth=1, relief="solid")
lb1.grid(row = 0, column = 0, columnspan = 2, sticky = 'ew')

enter_details = Label(window, text = "Please enter your details", height=6, bg = "white")
enter_details.grid(row = 1, column = 0, columnspan = 2, sticky = "ew")

input_name = Label(window, text = "Name:", bg = "white", fg = "black")
input_name.grid(row = 2, column = 0, sticky = "e")

e1 = Entry(window, borderwidth=1, relief="solid")
e1.grid(row = 2, column = 1, sticky = "w") 

input_age = Label(window, text = "Age:", bg = "white", fg = "black")
input_age.grid(row = 3, column = 0, sticky = "e", pady = 8)

e2 = Entry(window, borderwidth=1, relief="solid")
e2.grid(row = 3, column = 1, sticky = "w") 

b_continue = Button(window, text = "continue")
b_continue.grid(row = 4, column = 0, columnspan = 2, pady = 30)




window.mainloop()
