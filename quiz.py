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

    def exitbutton(self): #Clears the window and finds the accuracy of the user and displays their score and accuracy and the retry button
        self.questions.destroy()
        self.button_a.destroy()
        self.button_b.destroy()
        self.button_c.destroy()
        self.button_d.destroy()
        self.scorelbl.destroy()
        self.button_exit.destroy()
        try: #If the response label is there, it will destroy it else it won't do anything
            self.response.destroy()
        except AttributeError:
            ""
        try: #If the response label is there, it will destroy it else it won't do anything
            self.button.destroy()
        except AttributeError:
            ""
        try:
            self.accuracy = (self.correct / self.total) * 100 #Sets the variable to hold the accuracy%
        except ZeroDivisionError:
            self.accuracy = 0 #If the user has no questions answered, the accuracy is 0%
        self.accuracy = round(self.accuracy, 2)
        self.endscreen = Label(window, text = "Thank you for playing! You got " + str(self.correct) + "/" + str(self.total) + " correct.\n" + "Your accuracy is: " + str(self.accuracy) + "%", bg="white")
        self.endscreen.grid(row=1, columnspan = 2, column=0)
        self.buttoncreate("Continue", 2)
        self.button.config(text = "Retry")
        self.button.grid(row = 4, column = 0, columnspan = 2, pady = 30)
        
    def score(self): #This function displays a label with the score and creates two variables that increase when questions are answered and when questions are answered correctly
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
            self.buttoncreate("Continue", 2) #This creates another object that will lead to the quiz part of the program
            self.button.grid(row = 4, column = 0, columnspan = 2, pady = 30) #This places the button created by the class

    def instructions2(self): #This chooses a technique from the list, displays the question for the technique, creates and places buttons on the window that can be clicked as the answer
        self.button.destroy()
        try:
            self.endscreen.destroy()
        except AttributeError:
            ""
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
            self.scorelbl.config(text="Score: " + str(self.correct) + "/" + str(self.total))
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
            self.scorelbl.config(text="Score: " + str(self.correct) + "/" + str(self.total))
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

b_continue = ButtonClass()
b_continue.buttoncreate("Continue", 1)
b_continue.button.grid(row = 4, column = 0, columnspan = 2, pady = 30)

window.mainloop() #The end of the window





