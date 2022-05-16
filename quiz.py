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

question = random.choice(qlist)
print(question)

from tkinter import*
root = Tk()

#This code resizes the window and packs it inside the window
t1 = Text(root,width = 250, height = 9)
t1.pack()

t1.insert(END,qdict[question])

e1 = Entry(root)
e1.pack()

def enter(): 
    g = str(e1.get())
    if g == adict[question]:
        t1.insert(END,"yeah")
    else:
        t1.insert(END,"nah")



    
#def add():
    x = int(e1.get()) #Allows the entry of first number in entry box1
    t1.insert(END,)
    t1.insert(END,"\n")

b1 = Button(root,text = "Enter",command = enter)
b1.pack()












root.mainloop()

