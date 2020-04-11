
import tkinter as tk
import Crime
#from Crime import Entr
from tkinter import *

from tabulate import tabulate
def printSomething1():
    y = Crime.cooz()
    label = tk.Label(root,bg='green yellow', text= str(y))
    label.pack()
    
   
root = tk.Tk()

root.geometry('1000x500')
root.title('Crime Supect Prediction')
root.configure(background='Black')

button = tk.Button(root, text="Suspect in 1st pridiction",bg='turquoise', command=printSomething1)
button.pack()
root.mainloop()
