#################################### IMPORT LIBRARIES ############################################

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


data= pd.read_excel(r"C:\Users\Anurag\Desktop\Project\Ace\ACE.xlsx")
data=pd.DataFrame(data)
#print(data)

##################################################################################################


#################################Ignore Warning################################################################

import warnings
warnings.filterwarnings("ignore")


####################################### MACHINE LEARNING USING ALGORITHM ############################

from pandas.plotting import scatter_matrix
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


################# Training & Testing #####################
x_train = data[["Gender","Age","Latitude","Longitude","Weapon","Partner","Theft","Type of Crime"]] 
y_train = data[["Case ID"]] 
#print(x_train,y_train)

def alo(z):
    cls= KNeighborsClassifier(n_neighbors= 5,metric='minkowski',p=2)
    cls.fit(x_train,y_train)
    #z=[[1, 24, 28.7027136, 77.1939912, 2, 4, 3, 1]]
    y_pred=cls.predict(z)
    y_pred=int(y_pred)
    #print(y_pred)
    f=data[data["Case ID"]==y_pred ]
    u=f[["Aadhaar No","Name","Gender","Age","Guardian","Contact","Address"]]
    ind(u)

# Program to find most frequent 
# element in a list 

def most_frequent(case_id): 
	counter = 0
	num = case_id[0] 
	
	for i in case_id: 
		curr_frequency = case_id.count(i) 
		if(curr_frequency> counter): 
			counter = curr_frequency 
			num = i 
	return num 
 
from tabulate import tabulate
def ind(u):
     k=["Aadhaar No","Name","Gender","Age","Guardian","Contact","Address"]
     u.set_index('Aadhaar No',inplace=True)
     print(tabulate(u,headers=k))
     import Table as t
     t.app1(u)

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


             
