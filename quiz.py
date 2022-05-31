from distutils.command.build import build
from tkinter import *
from PIL import *
import random
import question_storage #Allows this file to access questions stored in another file

window = Tk() #Sets up GUI window
window.geometry("500x350") #Resizing window
window.title("Language Features Quiz") #Title for window
window.configure(bg = "white") #Configures the background colour
window.grid_columnconfigure(0,weight=1) #Sets how much the columns in the GUI window grow when the window is expanded
window.grid_columnconfigure(1,weight=1)

class ButtonClass: #Sets up a class called ButtonClass
    def __init__(self, name, version): #This function is called when the class is called and creates a button depending on the arguments provided
        self.name = name #These set the arguments provided to variables that can be accessed by the entire class
        self.version = version
        if self.name == "Continue" and self.version == 1: #Each of these will create a button that has a different command
            self.button = Button(window, text=self.name, command=self.instructions1)
        elif self.name == "Continue" and self.version == 2:
            self.button = Button(window, text=self.name, command=self.instructions2)
        else:
            self.button = Button(window, text=self.name, command=self.choices)

    def instructions1(self): #This function is called when a button is pressed
        global name
        global age
        name = (e1.get()) #Gets the value in the entry box
        try: #it sees if the values entered are valid, if so it then displays the instructions
            age = int(e2.get())
        except ValueError:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly") #These change an exisiting label's text to the error message
        if name == "":
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        if age < 0:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        else:
            b_continue2 = ButtonClass("Continue", 2) #This creates another object that will lead to the quiz part of the program
            b_continue2.button.grid(row = 4, column = 0, columnspan = 2, pady = 30) #This places the button created by the class

    def instructions2(self): #This chooses a technique from the list, displays the question for the technique, creates and places buttons on the window that can be clicked as the answer
        self.button.destroy()
        self.question = random.choice(question_storage.qlist)
        global questions
        global a
        global b
        global c
        global d
        questions = Label(window,text=question_storage.qdict[self.question], bg="white")
        questions.grid(row=1, column=0)
        a = ButtonClass("A", self.question)
        a.button.grid(row=2, column=0)
        b = ButtonClass("B", self.question)
        b.button.grid(row=3, column=0)
        c = ButtonClass("C", self.question)
        c.button.grid(row=4, column=0)
        d = ButtonClass("D", self.question)
        d.button.grid(row=5, column=0)

    def choices(self): #This is the function for each of the mutli-choice buttons, when clicked it will see if the answer matches with the button pressed, the button then displays whether it was correct, destroys itself and creates another button
        self.question = self.version
        global questions
        global a
        global b
        global c
        global d
        if self.name == question_storage.adict[self.question]: #When button pressed is incorrect, displays incorrect message and clears window
            self.response = Label(window,text="correct", bg="white")
            self.response.grid(row=5, column=0)
            questions.destroy()
            a.button.destroy()
            b.button.destroy()
            c.button.destroy()
            d.button.destroy()
            x = ButtonClass("Continue", 2)
            x.button.grid(row=6, column=0)

        else: #When button pressed is incorrect, displays incorrect message and clears window
            self.response = Label(window,text="incorrect", bg="white")
            self.response.grid(row=5, column=0)
            questions.destroy()
            a.button.destroy()
            b.button.destroy()
            c.button.destroy()
            d.button.destroy()
            x = ButtonClass("Continue", 2)
            x.button.grid(row=6, column=0)



x = ButtonClass("Continue", 2) #Calls the class and creates a object and button belonging to the object
x.button.grid(row=0, column=0) #Places the button on the window














window.mainloop()





