from  tkinter import *
import tkinter as tk
from tkinter import ttk

o = tk.Tk()
o.title('Criminal Suspect Prediction')
o.geometry("1000x700")

Tn = ttk.Label(o,text='Criminal Suspact Prediction')
Tn.grid(row=0,column=4,pady=5)

Tn = ttk.Label(o,text='Reqired Details :')
Tn.grid(row=1,column=0,pady=1)

ln = ttk.Label(o,text='Gender :')
ln.grid(row=2,column=0,pady=1)

tln =  ttk.Entry(o,width=30)
tln.grid(row=2,column=1,pady=1)

ln1 = ttk.Label(text='Age :')
ln1.grid(row=3,column=0,pady=1)

tln1 =  ttk.Entry(o,width=30)
tln1.grid(row=3,column=1,pady=1)

ln2 = ttk.Label(text='Block :')
ln2.grid(row=4,column=0,pady=1)

tln2 =  ttk.Entry(o,width=30)
tln2.grid(row=4,column=1,pady=1)

ln3 = ttk.Label(text='LandMark :')
ln3.grid(row=5,column=0,pady=1)

tln3 =  ttk.Entry(o,width=30)
tln3.grid(row=5,column=1,pady=1)

ln4 = ttk.Label(text='Area :')
ln4.grid(row=6,column=0,pady=1)

tln4 =  ttk.Entry(o,width=30)
tln4.grid(row=6,column=1,pady=1)

ln5 = ttk.Label(text='City :')
ln5.grid(row=7,column=0,pady=1)

tln5 =  ttk.Entry(o,width=30)
tln5.grid(row=7,column=1,pady=1)

ln6 = ttk.Label(text='Pin Code :')
ln6.grid(row=8,column=0,pady=1)

tln6 =  ttk.Entry(o,width=30)
tln6.grid(row=8,column=1,pady=1)


ln7 = ttk.Label(text='Weapon :')
ln7.grid(row=9,column=0,pady=1)

tln7 = ttk. Entry(o,width=30)
tln7.grid(row=9,column=1,pady=1)

ln8 = ttk.Label(text='Members :')
ln8.grid(row=10,column=0,pady=1)

tln8 =  ttk.Entry(o,width=30)
tln8.grid(row=10,column=1,pady=1)


ln9 = ttk.Label(text='Theft :')
ln9.grid(row=11,column=0,pady=1)

tln9 =  ttk.Entry(o,width=30)
tln9.grid(row=11,column=1,pady=1)

ln10 = ttk.Label(text='Type of crime :')
ln10.grid(row=12,column=0,pady=1)

tln10 =  ttk.Entry(o,width=30)
tln10.grid(row=12,column=1,pady=1)

msg = Label(text='You click on button ')
msg.grid(row=13,column=1)
def inputbyuser(y):
      import Crime 
      Crime.usqt(y)
def event():
    #print('you have clicked on button')
    ln = tln.get()
    ln1 = tln1.get()
    ln2 = tln2.get()
    ln3 = tln3.get()
    ln4 = tln4.get()
    ln5 = tln5.get()
    ln6 = tln6.get()
    ln7 = tln7.get()
    ln8= tln8.get()
    ln9 = tln9.get()
    ln10= tln10.get()
    
    fullname1 = [ln,ln1,ln2,ln3,ln4,ln5,ln6,ln7,ln8,ln9,ln10]
    fullname=[]
    for i in fullname1:
        fullname.append(int(i))
    #print('name is  ',fullname)
    #print(type(fullname))
    msg.configure(text="you have clicked on button :")
    inputbyuser(fullname)
    return fullname



b = ttk.Button(o,text='click me',command=event)
b.grid(row=14,column=0,pady=2)





o.mainloop()
