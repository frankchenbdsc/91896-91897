from distutils.command.build import build
from tkinter import *
from PIL import *
import random

#The dictionary that contains the questions
qdict = {
    "Allusion": """What is the Language Technique used here? Your new get rich
quick scheme is going to sink like the Titanic.
A: Allusion
B: Alliteration
C: Preposition
D: Metaphor
Answer: """,
    "Hyperbole": """What is the Language Technique used here? His eyes flew out
of his head.
A: Allusion
B: Hyperbole
C: Simile
D: Superlative
Answer: """,
    "Metaphor": """What is the Language Technique used here? He was the sun, everything
revolved around him.
A: Neologism
B: Interrogative
C: Metaphor
D: Coinage
Answer: """,
    "Simile": """What is the Language Technique used here? His hand was cold as ice.
A: Simile
B: Imperative
C: Abbreviation
D: Coinage
Answer: """,
    "Alliteration": """What is the Language Technique used here? The powerful punch pounded Peter.
A: Salutation
B: Verbs
C: Alliteration
D: Cliche
Answer: """,
    "Salutation": """What is the Language Technique used here? Hello!
A: Salutation
B: Interrogative
C: Comparative
D: Acronym
Answer: """,
    "Interrogative": """What is the Language Technique used here? What were you 
doing at 8:30am?
A: Jargon
B: Superlative
C: Interrogative
D: Preposition
Answer: """,
    "Imperative":  """What is the Language Technique used here? Go home!
A: Anecdote
B: Comparative
C: Contraction
D: Imperative
Answer: """,
    "Abbreviation": """What is the Language Technique used here? Dr., Prof.
A: Allusion
B: Abbreviation
C: Contraction
D: Imperative
Answer: """,
    "Triple-Construction": """What is the Language Technique used here? We will stand tall, we will not fall
and we will reclaim our land!
A: Allusion
B: Preposition
C: Contraction
D: Triple-Construction
Answer: """,
    "Verb": """What is the Language Technique used here? Run, jump, throw.
A: Allusion
B: Verbs
C: Personification
D: Imperative
Answer: """,
    "Superlative": """What is the Language Technique used here? The best, fastest, strongest.
A: Allusion
B: Verbs
C: Personification
D: Superlative
Answer: """,
    "Preposition": """What is the Language Technique used here? Below, on top, to the right.
A: Preposition
B: Contraction
C: Personification
D: Adjective
Answer: """,
    "Colloquialism": """What is the Language Technique used here? I 'ain't gonna' leave it at that.
A: Preposition
B: Contraction
C: Colloquialism
D: Adjective
Answer: """,
    "Personification": """What is the Language Technique used here? The chair let out a groan as 
Mr Turner's ample weight settled on top of it.
A: Preposition
B: Contraction
C: Personification
D: Endearment
Answer: """,
    "Cliche": """What is the Language Technique used here? Roses are red, violets are blue...
The apple doesn't fall far from the tree.
A: Cliche
B: Contraction
C: Personification
D: Endearment
Answer: """,
    "Onomatopoeia": """What is the Language Technique used here? Boom! Tick Tock
Ding Dong
A: Cliche
B: Onomatopoeia
C: Allegory
D: Endearment
Answer: """,
    "Comparative": """What is the Language Technique used here? Bigger, smaller, faster
A: Comparative
B: Onomatopoeia
C: Allegory
D: Endearment
Answer: """,
    "Contraction": """What is the Language Technique used here? He'd, He'll, Won't
A: Contraction
B: Onomatopoeia
C: Allegory
D: Endearment
Answer: """,
    "Euphemism": """What is the Language Technique used here? Kicked the bucket, departed, passed away
A: Contraction
B: Euphemism
C: Allegory
D: Endearment
Answer: """,
    "Anecdote": """What is this Language Technique? A short story to make people think
or laugh
A: Contraction
B: Euphemism
C: Anecdote
D: Endearment
Answer: """,
    "Allegory": """What is this Language Technique? A story where a hidden 
meaning can be interpreted.
A: Contraction
B: Euphemism
C: Anecdote
D: Allegory
Answer: """,
    "Jargon": """What is the Language Technique used here? AWOL, Financial Position,
Trade Statement, Gross Profit
A: Jargon
B: Euphemism
C: Allegory
D: Endearment
Answer: """,
    "Neologism": """What is this Language Technique? A mix of two words that forms a new word.
Smoke and fog make Smog.
A: Jargon
B: Neologism
C: Allegory
D: Endearment
Answer: """,
    "Irony": """What is the Language Technique used here? The car crashed against a drive safe sign.
A: Jargon
B: Euphemism
C: Irony
D: Endearment
Answer: """,
    "Endearment": """What is the Language Technique used here? Baby, Sweetheart, Sugar.
A: Jargon
B: Euphemism
C: Irony
D: Endearment
Answer: """,
    "Homophone": """What is the Language Technique used here? Bald, Bold, Reign, Rain
A: Homophone
B: Homonym
C: Irony
D: Endearment
Answer: """,
    "Homonym": """What is the Language Technique used here? 'Bear' with me.
A 'bear' is coming.
A: Homophone
B: Homonym
C: Irony
D: Endearment
Answer: """,
    "Adjective": """What is the Language Technique used here? Red, Fast, Happy
A: Homophone
B: Adjective
C: Irony
D: Coinage
Answer: """,
    "Acronym": """What is the Language Technique used here? USA (United States of America,
NSA (National Security Agency).
A: Acronym
B: Adjective
C: Irony
D: Coinage
Answer: """,
    "Coinage": """What is this Language Technique? A new word that a person made, Google
A: Acronym
B: Adjective
C: Irony
D: Coinage
Answer: """,
}

#Dictionary that contains answers
adict = {
    "Allusion": "A",
    "Hyperbole": "B",
    "Metaphor": "C",
    "Simile": "A",
    "Alliteration": "C",
    "Salutation": "A",
    "Interrogative": "C",
    "Imperative": "D",
    "Abbreviation": "B",
    "Triple-Construction": "D",
    "Verb": "B",
    "Superlative": "D",
    "Preposition": "A",
    "Colloquialism": "C",
    "Personification": "C",
    "Cliche": "A",
    "Onomatopoeia": "B",
    "Comparative": "A",
    "Contraction": "A",
    "Euphemism": "B",
    "Anecdote": "C",
    "Allegory": "D",
    "Jargon": "A",
    "Neologism": "B",
    "Irony": "C",
    "Endearment": "D",
    "Homophone": "A",
    "Homonym": "B",
    "Adjective": "B",
    "Acronym": "A",
    "Coinage": "D"
}

#List where words that correspond to the question dictionary can be selected from
qlist = ["Allusion", "Hyperbole", "Metaphor", "Simile", "Alliteration", "Salutation", "Interrogative", "Imperative", "Abbreviation", "Triple-Construction", "Verb", "Superlative", "Preposition", "Colloquialism", "Personification", "Cliche", "Onomatopoeia", "Comparative", "Contraction", "Euphemism", "Anecdote", "Allegory", "Jargon", "Neologism", "Irony", "Endearment", "Homophone", "Homonym", "Adjective", "Acronym", "Coinage"]

window = Tk()
window.geometry("500x350") #Resizing window
window.title("Language Features Quiz") #title
window.configure(bg = "white")
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)

class ButtonClass:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        if self.name == "Continue" and self.version == 1:
            self.button = Button(window, text=self.name, command=self.instructions1)
        elif self.name == "Continue" and self.version == 2:
            self.button = Button(window, text=self.name, command=self.instructions2)
        else:
            self.button = Button(window, text=self.name, command=self.choices)

    def instructions1(self):
        global name
        global age
        name = (e1.get()) #Gets the value in the entry box
        try:
            age = int(e2.get())
        except ValueError:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        if name == "":
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        if age < 0:
            enter_details.config(text = "The details entered may be incorrect, please make sure it is typed correctly")
        else:
            b_continue2 = ButtonClass("Continue", 2)
            b_continue2.button.grid(row = 4, column = 0, columnspan = 2, pady = 30)

    def instructions2(self):
        self.button.destroy()
        self.question = random.choice(qlist)
        global questions
        global a
        global b
        global c
        global d
        questions = Label(window,text=qdict[self.question], bg="white")
        questions.grid(row=1, column=0)
        a = ButtonClass("A", self.question)
        a.button.grid(row=2, column=0)
        b = ButtonClass("B", self.question)
        b.button.grid(row=3, column=0)
        c = ButtonClass("C", self.question)
        c.button.grid(row=4, column=0)
        d = ButtonClass("D", self.question)
        d.button.grid(row=5, column=0)

    def choices(self):
        self.question = self.version
        if self.name == adict[self.question]:
            response = Label(window,text="correct", bg="white")
            response.grid(row=6, column=0)
            global questions
            global a
            global b
            global c
            global d
            self.questions.destroy()
            self.a.button.destroy()
            self.b.button.destroy()
            self.c.button.destroy()
            self.d.button.destroy()
            x = ButtonClass("Continue", 2)
            x.button.grid(row=6, column=0)

        else:
            response = Label(window,text="incorrect", bg="white")
            response.grid(row=6, column=0)
            global questions
            global a
            global b
            global c
            global d
            questions.destroy()
            a.button.destroy()
            b.button.destroy()
            c.button.destroy()
            d.button.destroy()
            x = ButtonClass("Continue", 2)
            x.button.grid(row=6, column=0)


x = ButtonClass("Continue", 2)
x.button.grid(row=0, column=0)














window.mainloop()





