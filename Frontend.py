
'''
from  tkinter import *
from Crime import output


o = Tk()
o.title('Crime Supect Prediction')
o.geometry("1000x700")



fn = Label(text='enter fname :', fg="blue")
fn.pack()

#tfn =  Entry()
#tfn =  u
#tfn.pack()



ln = Label(text='enter lname :')
ln.pack()


#tln =  Entry()
#tln =v
#tln.pack()

msg = Label(text='jgghf')
msg.pack()
#o.grid(msg,0,1)
c=output()
def event():
    print('you have clicked on button')
    #fn = tfn.get()
    #ln = tln.get()
    fullname = c
    print('name is  ',fullname)
    msg.configure(text=fullname)
    

b = Button(text='click me',command=event)
b.pack()


o.mainloop()

'''

import tkinter as tk
import Crime
#from Crime import Entr
from tkinter import *
'''
def server_get(event):

    text=entry.get()
    #text1=entry.get()
    
    client.send_message(text)
    #client.send_message(text1)

client=Entr()
client.connected()
'''

from tabulate import tabulate
def printSomething1():
    y = Crime.cooz()
    label = tk.Label(root,bg='green yellow', text= str(y))
    label.pack()
    
"""
def printSomething2(): 
    z = Crime.tooz()
    label = tk.Label(root, text= str(z),bg='lime green')
    label.pack()
"""    
root = tk.Tk()

#v=tk.StringVar()
'''
text1=Text(root,height=25,width=125,bg='black', fg='yellow')
scroll=Scrollbar(root,command=text1.yview,orient=VERTICAL)
scroll.config(command=text1.yview)
text1.configure(yscrollcommand=scroll.set)
fn = Label(text='enter fname :', fg="blue")
fn.pack()
entry=Entry(root,textvariable=v,bg='white',fg='black')
entry.pack()
#entry.focus()
ln = Label(text='enter lname :')
ln.pack()
entry1=Entry(root,textvariable=v,bg='white',fg='black')
entry1.pack()
#entry1.focus()
text1.pack(side=LEFT,fill=BOTH,expand='YES')
scroll.pack(side=RIGHT,fill=BOTH)
entry.bind('<Return>',server_get)
entry1.bind('<Return>',server_get)
'''

root.geometry('1000x500')
root.title('Crime Supect Prediction')
root.configure(background='Black')
'''
fn = Label(text='enter fname :', fg="black")
fn.pack()
entry=Entry(bg='white',fg='black')
entry.pack()
#entry.focus()
ln = Label(text='enter lname :')
ln.pack()

entry1=Entry(bg='white',fg='black')
entry1.pack()


def Lt1():
    L=[]
    L.append(entry)
    L.append(entry1)
    return L
    
    


#entry1.focus()
entry.bind('<Return>',server_get)
#entry1.bind('<Return>',server_get)
'''

button = tk.Button(root, text="Suspect in 1st pridiction",bg='turquoise', command=printSomething1)
button.pack()
#button = tk.Button(root, text="Suspect in 2st pridiction",bg='turquoise', command=printSomething2)
#button.pack()
root.mainloop()
