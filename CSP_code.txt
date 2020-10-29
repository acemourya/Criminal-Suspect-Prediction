import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


data= pd.read_excel(r"Data Path")
data=pd.DataFrame(data)
#print(data)

################################################################################


############################# Ignore Warning####################################

import warnings
warnings.filterwarnings("ignore")


############################ MACHINE LEARNING USING ALGORITHM ##################


from sklearn.cluster import KMeans
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

from tkinter import Tk,StringVar,ttk
from tkinter import *
from tkinter import messagebox
import time;
import datetime



############ Training & Testing ######################

x_train = data[["Gender","Age","Latitude","Longitude","Weapon","Partner","Theft","Type of Crime"]] 
y_train = data[["Case ID"]] 
#print(x_train,y_train)
from pandastable import Table, TableModel
def smmm(u):
    #f.grid(row=15,column=0,sticky=W,ipadx=600,ipady=17)
 
    df = TableModel.getSampleData()
    pt = Table(leftFrame2,dataframe=u,showtoolbar=True, showstatusbar=True)
    pt.grid(row=15,column=0,sticky=W,ipadx=345,ipady=17)
    pt.show()
from tabulate import tabulate
def ind(u):
     k=["Aadhaar No","Name","Gender","Age","Guardian","Contact","Address","Latitude","Longitude","Latitude_C","Longitude_C"]
     u.set_index('Aadhaar No',inplace=True)
     print(tabulate(u,headers=k)) 
     smmm(u)
    
        
def alo(z):
    cls= KNeighborsClassifier(n_neighbors= 5,metric='minkowski',p=2)
    cls.fit(x_train,y_train)
    cls1 = LinearRegression().fit(x_train,y_train)
    cls2 = LogisticRegression(solver='liblinear', random_state=0).fit(x_train,y_train)
    cls3 = KMeans(n_clusters=7)
    cls3.fit(x_train,y_train)
    z1=[[1, 24, 28.7027136, 77.1939912, 2, 4, 3, 1]]
    y_pred1=cls1.predict(z1)
    y_pred1=int(y_pred1)
    y_pred2=cls2.predict(z1)
    y_pred2=int(y_pred2)
    y_pred3=cls3.predict(z1)
    y_pred3=int(y_pred3)
    y_pred=cls.predict(z)
    y_pred=int(y_pred)
    print(y_pred,y_pred1,y_pred2,y_pred3,)
    f=data[data["Case ID"]==y_pred]
    u=f[["Aadhaar No","Name","Gender","Age","Guardian","Contact","Address","Latitude","Longitude","Latitude_C","Longitude_C"]]
    ind(u)
    
# Program to find most frequent element in a list 

def most_frequent(case_id): 
	counter = 0
	num = case_id[0] 
	
	for i in case_id: 
		curr_frequency = case_id.count(i) 
		if(curr_frequency> counter): 
			counter = curr_frequency 
			num = i 
	return num

######################################################################################

########################## Front tent GUI ############################################
    

############## Framing ################

root=Tk()
root.title('Criminal Suspect Prediction')
root.iconbitmap(r'Icon\faviconn.ico')
root.geometry('1600x850+0+0')
root.configure(bg='black')
leftFrame3=Frame(root,width=1600,height=50,bd=2,relief='raise')
leftFrame3.pack(side=TOP)
leftFrame=Frame(root,width=1150,height=800,bd=2,relief='raise')
leftFrame.pack(side=LEFT)
RightFrame=Frame(root,width=450,height=800,bd=2,relief='raise')
RightFrame.pack(side=RIGHT)

leftFrameL=Frame(leftFrame,width=1150,height=400,bd=4,relief='raise')
leftFrameL.pack(side=TOP)
leftFrame1=Frame(leftFrameL,width=200)
leftFrame1.pack(side=LEFT)
leftFrame12=Frame(leftFrameL,width=788)
leftFrame12.pack(side=RIGHT)
leftFrame2=Frame(leftFrame,width=1150,height=450,bd=4,relief='raise')
leftFrame2.pack(side=TOP)

RightFrame1=Frame(RightFrame,width=450,height=400,bg="azure",bd=4,relief='raise')
RightFrame1.pack(side=TOP)
RightFrame2=Frame(RightFrame,width=450,height=400,bg="azure",bd=4,relief='raise')
RightFrame2.pack(side=TOP)
    
##########################################

from PIL import ImageTk,Image

my_img=ImageTk.PhotoImage(Image.open(r'Images\image.png'))
my_label1=Label(RightFrame1,image=my_img,bg="#D4F3EF")
my_label1.grid(row=0,column=0,ipadx=75,ipady=40)

my_img1=ImageTk.PhotoImage(Image.open(r'Images\images(13).png'))
my_img2=ImageTk.PhotoImage(Image.open(r'Images\img2.png'))
my_img3=ImageTk.PhotoImage(Image.open(r'Images\img4.png'))
my_img4=ImageTk.PhotoImage(Image.open(r'Images\images(30).png'))
my_img5=ImageTk.PhotoImage(Image.open(r'Images\img4.png'))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

my_label=Label(RightFrame2,image=my_img1,bg="#D4F3EF")
my_label.grid(row=0,column=0,columnspan=2,ipadx=75,ipady=70)



def usqt(y):
    z=[y]
    #print("pass",z)
    alo(z)
    
def cooz():  
    return u

def tooz():
    return v

def main():
    return cooz()
    return tooz()     
           

from  tkinter import *
import tkinter as tk
from tkinter import ttk
def Take_Inpt():
    
    Tn = Label(leftFrame3,font=('arial',20,'bold'),bg='#A6DCEF',text='CRIMINAL SUSPECT PREDICTION')
    Tn.grid(row=0,column=4,sticky=W,ipadx=600,ipady=17)

    Tn = Label(leftFrame1,font=('arial',10,'bold'),text='Required Details :')
    Tn.grid(row=1,column=0,sticky=W,ipadx=10,pady=1)

    ln = Label(leftFrame1,text='Gender :')
    ln.grid(row=2,column=0,sticky=W,ipadx=10,pady=1)

    tln =  Entry(leftFrame1,width=30)
    tln.grid(row=2,column=1,sticky=W,pady=1)
 
    ln1 = Label(leftFrame1,text='Age :')
    ln1.grid(row=3,column=0,sticky=W,ipadx=10,pady=1)

    tln1 = Entry(leftFrame1,width=30)
    tln1.grid(row=3,column=1,sticky=W,pady=1)

    ln2 = Label(leftFrame1,text='LandMark :')
    ln2.grid(row=4,column=0,sticky=W,ipadx=10,pady=1)

    tln2 =  Entry(leftFrame1,width=30)
    tln2.grid(row=4,column=1,sticky=W,pady=1)
    """
    ln3 = ttk.Label(text='Area :')
    ln3.grid(row=5,column=0,pady=1)
    tln3 =  ttk.Entry(o,width=30)
    tln3.grid(row=5,column=1,pady=1)
    """
    ln4 = Label(leftFrame1,text='City :')
    ln4.grid(row=6,column=0,sticky=W,ipadx=10,pady=1)

    tln4 = Entry(leftFrame1,width=30)
    tln4.grid(row=6,column=1,sticky=W,pady=1)

    ln5 = Label(leftFrame1,text='Pin Code :')
    ln5.grid(row=7,column=0,sticky=W,ipadx=10,pady=1)

    tln5 =  Entry(leftFrame1,width=30)
    tln5.grid(row=7,column=1,sticky=W,pady=1)

    ln6 = Label(leftFrame1,text='State :')
    ln6.grid(row=8,column=0,sticky=W,ipadx=10,pady=1)

    tln6 =  Entry(leftFrame1,width=30)
    tln6.grid(row=8,column=1,sticky=W,pady=1)


    ln7 = Label(leftFrame1,text='Weapon :')
    ln7.grid(row=9,column=0,sticky=W,ipadx=10,pady=1)

    tln7 = Entry(leftFrame1,width=30)
    tln7.grid(row=9,column=1,sticky=W,pady=1)

    ln8 = Label(leftFrame1,text='Members Involve :')
    ln8.grid(row=10,column=0,sticky=W,ipadx=10,pady=1)

    tln8 =  Entry(leftFrame1,width=30)
    tln8.grid(row=10,column=1,sticky=W,pady=1)


    ln9 = Label(leftFrame1,text='Theft :')
    ln9.grid(row=11,column=0,sticky=W,ipadx=10,pady=1)

    tln9 =  Entry(leftFrame1,width=30)
    tln9.grid(row=11,column=1,sticky=W,pady=1)

    ln10 = Label(leftFrame1,text='Type of crime :')
    ln10.grid(row=12,column=0,sticky=W,ipadx=10,pady=1)

    tln10 =  Entry(leftFrame1,width=30)
    tln10.grid(row=12,column=1,sticky=W,pady=1)

    msg = Label(leftFrame1,text='You click on button ')
    msg.grid(row=13,column=1)

    
    pt = Label(leftFrame2,text='\"Predictive policing is the collection \n and analysis of data about previous crimes \n for identification and statistical prediction of individuals \n or geospatial areas with an increased probability of criminal activity \n to help developing policing intervention and prevention strategies \n and tactics.\"',font=('arial',20,'bold'))
    pt.grid(row=15,column=0,sticky=W,ipadx=114,ipady=100)


    def forward(image_number):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label=Label(RightFrame2,image=image_list[image_number-1])
        button_foward=Button(RightFrame2,text=">>",command=lambda:forward(image_number+1))
        button_back=Button(RightFrame2,text="<<",command=lambda:forward(image_number-1))
        if image_number==5:
            button_foward=Button(RightFrame2,text=">>",state=DISABLED)
        my_label.grid(row=0,column=0,columnspan=3,ipadx=100,ipady=70)    
        
        
    def back(image_number):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label=Label(RightFrame2,image=image_list[image_number-1])
        button_foward=Button(RightFrame2,text=">>",command=lambda:forward(image_number+1))
        button_back=Button(RightFrame2,text="<<",command=lambda:forward(image_number-1))
        if image_number==1:
            button_foward=Button(RightFrame2,text=">>",state=DISABLED)
        my_label.grid(row=0,column=0,columnspan=3,ipadx=100,ipady=70)
       
        

    button_back=Button(RightFrame2,text="<<",command=lambda:back(1))
    #button_exit=Button(RightFrame2,text="Exit ",command=root.quit)
    button_foward=Button(RightFrame2,text=">>",command=lambda:forward(5))

    button_back.grid(row=1,column=0,ipadx=50,sticky=W)
    button_foward.grid(row=1,column=1,ipadx=50,sticky=E)
                    
    def inputbyuser(y):
         
        usqt(y)
    def event():
        #print('you have clicked on button')
        ln = tln.get()
        ln1 = tln1.get()
        ln2 = tln2.get()
        
        ln4 = tln4.get()
        ln5 = tln5.get()
        ln6 = tln6.get()
        ln7 = tln7.get()
        ln8= tln8.get()
        ln9 = tln9.get()
        ln10= tln10.get()
    
        ln_add=ln2+" "+ln4+" "+ln5+" "+ln6
        Gender={'Female':0,'Male':1,'Other':2}
        ln=Gender[ln]
        Weapon={'Other':0,'Nothing':1,'Knife':2,'Gun':3}
        ln7=Weapon[ln7]
        Theft={'Other':0,'Money':1,'Mobile':2,'Jewellery':3,'Bike':4,'Car':5}
        ln9=Theft[ln9]
        ToC={'Other':0,'Snaching':1,'Burglary':2,'Robbery':3,'Assault':4,'Extortion':5}
        ln10=ToC[ln10]
    
        import folium
        from folium import plugins
        import ipywidgets
        import geocoder
        import geopy
        from vega_datasets import data as vds

        address = geocoder.osm(ln_add)
        #print(address.json)
        address_latlng = [address.lat, address.lng]   
    
        fullname1 = [ln,ln1,address.lat, address.lng,ln7,ln8,ln9,ln10]
        fullname=[]
        for i in fullname1: 
            fullname.append(i)
        msg.configure(text="you have clicked on button :")
        pt.grid_remove()
        inputbyuser(fullname)
        return fullname

    b = Button(leftFrame1,fg='black',width=20,
                font=('arial',10,'bold'),text='Click me',command=event)
    b.grid(row=14,column=0,pady=2)
    root.mainloop()
Take_Inpt()
        
