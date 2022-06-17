from distutils.command.build import build
from tkinter import *
import random
import question_storage #Allows this file to access questions stored in another file
import json

window = Tk() #Sets up GUI window
window.geometry("400x300") #Resizing window
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
                self.button = Button(window, text=self.name, bg = "white", borderwidth=1, relief="solid", command=self.instructions1)
            elif self.version == 2:
                self.button = Button(window, text=self.name, bg = "white", borderwidth=1, relief="solid", command=self.instructions2)
            elif self.version == 3:
                self.button = Button(window, text=self.name, bg = "white", borderwidth=1, relief="solid", command=self.instructions3)
        elif self.name == "Button":
            if self.version == "A":
                self.button_a = Button(window, text=self.version, bg = "white", borderwidth=1, relief="solid", width = 8, command=lambda:self.choices("A"))
            elif self.version == "B":
                self.button_b = Button(window, text=self.version, bg = "white", borderwidth=1, relief="solid", width = 8, command=lambda:self.choices("B"))
            elif self.version == "C":
                self.button_c = Button(window, text=self.version, bg = "white", borderwidth=1, relief="solid", width = 8, command=lambda:self.choices("C"))
            elif self.version == "D":
                self.button_d = Button(window, text=self.version, bg = "white", borderwidth=1, relief="solid", width = 8, command=lambda:self.choices("D"))
            elif self.version == "Exit":
                self.button_exit = Button(window, text=self.version, bg = "white", borderwidth=1, relief="solid", width = 8, command=self.exitbutton)

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
        
        try: #This section sees if the score is higher than the highscore stored and if so, it will update the highscore
            with open(r"userdetails.json", "r") as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError as e:
            data = {}
            print(e)
        yikes = open(r"userdetails.json", "a+")
        try:
            if data[str(self.username)]["highscorecorrect"] < self.correct:
                data[str(self.username)] = None
                data[str(self.username)] = {"name": self.username, "age": self.age, "highscorecorrect": self.correct, "highscoretotal": self.total}
        except:
            data[str(self.username)] = None
            data[str(self.username)] = {"name": self.username, "age": self.age, "highscorecorrect": self.correct, "highscoretotal": self.total}
        with open(r"userdetails.json", "w") as file:
                json.dump(data, file, indent=4) #Updates the JSON file
        #Shows statistics and score with the retry button
        self.endscreen = Label(window, text = "Thank you for playing {}! You got ".format(self.username) + str(self.correct) + "/" + str(self.total) + " correct.\n" + "Your accuracy is: " + str(self.accuracy) + "%" "\nYour high score is: " + str(data[str(self.username)]["highscorecorrect"]) + "/" + str(data[str(self.username)]["highscoretotal"]) + ".", bg="white")
        self.endscreen.grid(row=1, columnspan = 2, column=0, pady = 10)
        self.buttoncreate("Continue", 2)
        self.button.config(text = "Retry")
        self.button.grid(row = 4, column = 0, columnspan = 2, pady = 25)
        
    def score(self): #This function displays a label with the score and creates two variables that increase when questions are answered and when questions are answered correctly
        self.correct = 0
        self.total = 0
        self.scorelbl = Label(window, text= "Score: " + str(self.correct) + "/" + str(self.total) , bg="white", borderwidth=1, relief="solid")
        self.scorelbl.grid(row=6, column=1, sticky="SE", pady = 15)

    def choices(self, choice): #This is the function for each of the mutli-choice buttons, when clicked it will see if the answer matches with the button pressed, the button then displays whether it was correct, destroys itself and creates another button
        if choice == question_storage.adict[self.question]: #When button pressed is incorrect, displays incorrect message and clears window
            self.response = Label(window,text="That was correct!", bg="white", height = 5)
            self.response.grid(row=2, column=0, columnspan = 2)
            self.correct += 1
            self.total += 1
            self.scorelbl.config(text="Score: " + str(self.correct) + "/" + str(self.total))
            self.questions.destroy()
            self.button_a.destroy()
            self.button_b.destroy()
            self.button_c.destroy()
            self.button_d.destroy()
            self.buttoncreate("Continue", 3)
            self.button.grid(row=3, column=0, columnspan = 2) #Places the button on the window

        else: #When button pressed is incorrect, displays incorrect message and clears window
            self.response = Label(window,text="That was incorrect, the answer was: " + str(self.question), bg="white", height = 5)
            self.response.grid(row=2, column=0, columnspan = 2)
            self.total += 1
            self.scorelbl.config(text="Score: " + str(self.correct) + "/" + str(self.total))
            self.questions.destroy()
            self.button_a.destroy()
            self.button_b.destroy()
            self.button_c.destroy()
            self.button_d.destroy()
            self.buttoncreate("Continue", 3)
            self.button.grid(row=3, column=0, columnspan = 2) #Places the button on the window
   
    def instructions1(self): #This function is called when a button is pressed
        self.username = (e1.get()) #Gets the value in the entry box
        try: #it sees if the values entered are valid, if so it then displays the instructions
            self.age = int(e2.get())
        except ValueError:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly") #These change an exisiting label"s text to the error message
        if self.name == "":
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        if self.age < 0:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        else:
            try: #Sees if the user already exists if not, it creates a dictionary in the JSON file
                with open(r"userdetails.json", "r") as file:
                    data = json.load(file)
            except json.decoder.JSONDecodeError as e:
                data = {}
                print(e)
            yikes = open(r"userdetails.json", "a+")
            if str(self.username) not in data:
                data[str(self.username)] = []
                data[str(self.username)].append(
                    {"name": self.username, "age": self.age}
                )
                with open(r"userdetails.json", "w") as file:
                    json.dump(data, file, indent=4)

            e1.destroy() #Clears the screen and displays instructions before the user continues
            e2.destroy()
            input_name.destroy()
            input_age.destroy()
            b_continue.button.destroy()
            enter_details.config(text = "This quiz is multi-choice and will keep asking questions until you exit.\n You will be provided with an example of a language \ntechnique and you will have to identify \nit by answering with one of the four choices.")
            self.buttoncreate("Continue", 2) #This creates another object that will lead to the quiz part of the program
            self.button.grid(row = 4, column = 0, columnspan = 2, pady = 30) #This places the button created by the class

    def instructions2(self): #This chooses a technique from the list, displays the question for the technique, creates and places buttons on the window that can be clicked as the answer
        self.button.destroy()
        try:
            self.endscreen.destroy()
        except AttributeError:
            ""
        try:
            enter_details.destroy()
        except AttributeError:
            ""
        self.question = random.choice(question_storage.qlist)
        self.questions = Label(window,text=question_storage.qdict[self.question], bg="white")
        self.questions.grid(row=2, columnspan = 2, column=0, pady = 3)
        self.buttoncreate("Button", "A")
        self.button_a.grid(row=3, column=0, sticky = "e", padx = 12, pady = 10)
        self.buttoncreate("Button", "B")
        self.button_b.grid(row=3, column=1, sticky = "w", padx = 12, pady = 10)
        self.buttoncreate("Button", "C")
        self.button_c.grid(row=4, column=0, sticky = "e", padx = 12, pady = 5)
        self.buttoncreate("Button", "D")
        self.button_d.grid(row=4, column=1, sticky = "w", padx = 12, pady = 5)
        self.score()
        self.buttoncreate("Button", "Exit")
        self.button_exit.grid(row=6, column=0, sticky = "w", pady = 15)

    def instructions3(self): #This chooses a technique from the list, displays the question for the technique, creates and places buttons on the window that can be clicked as the answer
        self.response.destroy()
        self.button.destroy()
        self.question = random.choice(question_storage.qlist)
        self.questions = Label(window,text=question_storage.qdict[self.question], bg="white")
        self.questions.grid(row=1, columnspan = 2, column=0, pady = 3)
        self.buttoncreate("Button", "A")
        self.button_a.grid(row=3, column=0, sticky = "e", padx = 12, pady = 10)
        self.buttoncreate("Button", "B")
        self.button_b.grid(row=3, column=1, sticky = "w", padx = 12, pady = 10)
        self.buttoncreate("Button", "C")
        self.button_c.grid(row=4, column=0, sticky = "e", padx = 12, pady = 5)
        self.buttoncreate("Button", "D")
        self.button_d.grid(row=4, column=1, sticky = "w", padx = 12, pady = 5)

#The lines of code underneath sets up labels, entry boxes and the first continue button in the GUI window

lb1 = Label(window, text = "Language Features Quiz", bg = "white", fg = "black", borderwidth=1, relief="solid")
lb1.grid(row = 0, column = 0, columnspan = 2, sticky = "ew")

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





