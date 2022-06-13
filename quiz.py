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
    def buttoncreate(self, name, version): #This function is called when the class is called and creates a button depending on the arguments provided
        self.name = name #These set the arguments provided to variables that can be accessed by the entire class
        self.version = version
        if self.name == "Continue":
            if self.version == 1: #Each of these will create a button that has a different command
                self.button = Button(window, text=self.name, command=self.instructions1)
            elif self.version == 2:
                self.button = Button(window, text=self.name, command=self.instructions2)
            elif self.version == 3:
                self.button = Button(window, text=self.name, command=self.instructions3)
        elif self.name == "Button":
            if self.version == "A":
                self.button_a = Button(window, text=self.version, command=lambda:self.choices("A"))
            elif self.version == "B":
                self.button_b = Button(window, text=self.version, command=lambda:self.choices("B"))
            elif self.version == "C":
                self.button_c = Button(window, text=self.version, command=lambda:self.choices("C"))
            elif self.version == "D":
                self.button_d = Button(window, text=self.version, command=lambda:self.choices("D"))
            elif self.version == "Exit":
                self.button_exit = Button(window, text=self.version, command=self.exitbutton)

    def exitbutton(self):
        self.questions.destroy()
        self.button_a.destroy()
        self.button_b.destroy()
        self.button_c.destroy()
        self.button_d.destroy()
        self.scorelbl.destroy()
        self.button_exit.destroy()
        endscreen = Label(window, text = "Thank you for playing! You got " + str(self.correct) + "/" + str(self.total) + " correct!", bg="white")
        endscreen.grid(row=1, columnspan = 2, column=0)
        self.buttoncreate("Continue", 2)
        self.button.config(text = "Retry")
        self.button.grid(row = 4, column = 0, columnspan = 2, pady = 30)


    def score(self):
        self.correct = 0
        self.total = 0
        self.scorelbl = Label(window, text= "Score: " + str(self.correct) + "/" + str(self.total) , bg="white", borderwidth=1, relief="solid")
        self.scorelbl.grid(row=6, column=1, sticky="SE")
   
    def instructions1(self): #This function is called when a button is pressed
        self.name = (e1.get()) #Gets the value in the entry box
        try: #it sees if the values entered are valid, if so it then displays the instructions
            self.age = int(e2.get())
        except ValueError:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly") #These change an exisiting label's text to the error message
        if self.name == "":
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        if self.age < 0:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        else:
            b_continue2 = ButtonClass("Continue", 2) #This creates another object that will lead to the quiz part of the program
            b_continue2.button.grid(row = 4, column = 0, columnspan = 2, pady = 30) #This places the button created by the class

    def instructions2(self): #This chooses a technique from the list, displays the question for the technique, creates and places buttons on the window that can be clicked as the answer
        self.button.destroy()
        self.question = random.choice(question_storage.qlist)
        self.questions = Label(window,text=question_storage.qdict[self.question], bg="white")
        self.questions.grid(row=1, columnspan = 2, column=0)
        self.buttoncreate("Button", "A")
        self.button_a.grid(row=2, column=0)
        self.buttoncreate("Button", "B")
        self.button_b.grid(row=3, column=0)
        self.buttoncreate("Button", "C")
        self.button_c.grid(row=4, column=0)
        self.buttoncreate("Button", "D")
        self.button_d.grid(row=5, column=0)
        self.score()
        self.buttoncreate("Button", "Exit")
        self.button_exit.grid(row=6, column=0)

    def choices(self, choice): #This is the function for each of the mutli-choice buttons, when clicked it will see if the answer matches with the button pressed, the button then displays whether it was correct, destroys itself and creates another button
        if choice == question_storage.adict[self.question]: #When button pressed is incorrect, displays incorrect message and clears window
            self.response = Label(window,text="correct", bg="white")
            self.response.grid(row=5, column=0)
            self.correct += 1
            self.total += 1
            self.score.config(text="Score: " + str(self.correct) + "/" + str(self.total))
            self.questions.destroy()
            self.button_a.destroy()
            self.button_b.destroy()
            self.button_c.destroy()
            self.button_d.destroy()
            self.buttoncreate("Continue", 3)
            self.button.grid(row=0, column=0) #Places the button on the window

        else: #When button pressed is incorrect, displays incorrect message and clears window
            self.response = Label(window,text="incorrect", bg="white")
            self.response.grid(row=5, column=0)
            self.total += 1
            self.score.config(text="Score: " + str(self.correct) + "/" + str(self.total))
            self.questions.destroy()
            self.button_a.destroy()
            self.button_b.destroy()
            self.button_c.destroy()
            self.button_d.destroy()
            self.buttoncreate("Continue", 3)
            self.button.grid(row=0, column=0) #Places the button on the window

    def instructions3(self): #This chooses a technique from the list, displays the question for the technique, creates and places buttons on the window that can be clicked as the answer
        self.response.destroy()
        self.button.destroy()
        self.question = random.choice(question_storage.qlist)
        self.questions = Label(window,text=question_storage.qdict[self.question], bg="white")
        self.questions.grid(row=1, column=0)
        self.buttoncreate("Button", "A")
        self.button_a.grid(row=2, column=0)
        self.buttoncreate("Button", "B")
        self.button_b.grid(row=3, column=0)
        self.buttoncreate("Button", "C")
        self.button_c.grid(row=4, column=0)
        self.buttoncreate("Button", "D")
        self.button_d.grid(row=5, column=0)

x = ButtonClass() #Creates a class
x.buttoncreate("Continue", 2)
x.button.grid(row=0, column=0) #Places the button on the window














window.mainloop()





