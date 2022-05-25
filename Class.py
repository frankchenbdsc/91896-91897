from distutils.command import config
from tkinter import *
from PIL import *
import random

window = Tk()
window.geometry("500x350") #Resizing window
window.title("Language Features Quiz") #title
window.configure(bg = "white")
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)

class MyClass:
  def __init__(self, name):
      self.name = name
      self.button = Button(window, text=self.name, padx=10)
      print(self.name)

y = MyClass("go")
y.button.pack()

#y = MyClass()
#print(y.x)


window.mainloop()
