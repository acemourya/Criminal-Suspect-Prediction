from tkinter import *
from pandastable import Table, TableModel
import tkinter as tk
from tkinter import ttk

def app1(u):
    #print("U  :",u)
    y=u
    #print("Y  :",y)
    sm(y)

def sm(y):
    #print("Passsss :",y)
    class TestApp(ttk.Frame):
         #import Crime
         #y=Crime.cooz()
         '''Basic test frame for the table'''
         def __init__(self, parent=None):
                self.parent = parent
                Frame.__init__(self)
                self.main = self.master
                #width_value=self.main.winfo_screenwidth()
                #height_value=self.main.winfo_screenheight()                
                self.main.geometry('1000x750+200+100')
                self.main.title('Crime Suspact Predicted')
                f = ttk.Frame(self.main)
                f.grid(row=15,columnspan=10,sticky=E+W)
                df = TableModel.getSampleData()
                self.table = pt = Table(f, dataframe=y,
                                        showtoolbar=True, showstatusbar=True)

                pt.show()
                return
    app=TestApp()       
    app.mainloop()
    
#app = TestApp()
#launch the app
#app.mainloop()
