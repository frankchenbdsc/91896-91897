from distutils.command import config #imports libraries
from tkinter import *
import random

window = Tk() #Sets up the GUI window
window.geometry("500x350") #Resizing window
window.title("Language Features Quiz") #title
window.configure(bg = "white") #Configures the background colour
window.grid_columnconfigure(0,weight=1) #Sets how much the columns in the GUI window grow when the window is expanded
window.grid_columnconfigure(1,weight=1)

class ButtonClass: #Sets up a class called ButtonClass
    def __init__(self, name, version): #This function is called when the class is called and creates a button depending on the arguments provided
        self.name = name
        self.version = version
        if self.name == "Continue" and self.version == 1: #Each of these will create a button that has a different command
            self.button = Button(window, text=self.name, command=self.instructions1)
        elif self.name == "Continue" and self.version == 2:
            self.button = Button(window, text=self.name, command=self.instructions2)
        else:
            self.button = Button(window, text=self.name, command=self.instructions2)

    def instructions1(self): #This function is called when a button is pressed
        name = (e1.get()) #Gets the value in the entry box
        try: #it sees if the values entered are valid, if so it then displays the instructions
            age = int(e2.get())
        except ValueError:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        if name == "":
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        if age < 0:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        else:
            e1.destroy()
            e2.destroy()
            input_name.destroy()
            input_age.destroy()
            b_continue.button.destroy()
            enter_details.config(text = "This quiz is multi-choice. You will be provided with an example of a language technique \nand you will have to identify it by answering with one of the four choices.")
            b_continue2 = ButtonClass("Continue", 2)
            b_continue2.button.grid(row = 4, column = 0, columnspan = 2, pady = 30)

#The lines of code underneath sets up labels, entry boxes and the first continue button in the GUI window

lb1 = Label(window, text = "Language Features Quiz", bg = "white", fg = "black", borderwidth=1, relief="solid")
lb1.grid(row = 0, column = 0, columnspan = 2, sticky = 'ew')

enter_details = Label(window, text = "Please enter your details before participating in the quiz", height=6, bg = "white")
enter_details.grid(row = 1, column = 0, columnspan = 2, sticky = "ew")

input_name = Label(window, text = "Name:", bg = "white", fg = "black")
input_name.grid(row = 2, column = 0, sticky = "e")

e1 = Entry(window, borderwidth=1, relief="solid")
e1.grid(row = 2, column = 1, sticky = "w") 

input_age = Label(window, text = "Age:", bg = "white", fg = "black")
input_age.grid(row = 3, column = 0, sticky = "e", pady = 8)

e2 = Entry(window, borderwidth=1, relief="solid")
e2.grid(row = 3, column = 1, sticky = "w") 

b_continue = ButtonClass("Continue", 1)
b_continue.button.grid(row = 4, column = 0, columnspan = 2, pady = 30)


window.mainloop() 
