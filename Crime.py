#################################### IMPORT LIBRARIES ############################################

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


data= pd.read_excel(r"C:\Users\Anurag\Desktop\Project\Data - Copy (2).xlsx")
data=pd.DataFrame(data)
#print(data)

##################################################################################################



##################################### DATA SET ###################################################


#data=data.head(23)
X1=data[["Gender","Weapon","Theft","Type of Crime"]]

#print(X1)

class MultiColumnLabelEncoder:
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here

    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)

p=MultiColumnLabelEncoder(columns = X1).fit_transform(data)
#print(p)
LM_match=pd.DataFrame(p)

#####################################################################################################

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



#split data
data1 = p #convert to dataframe to list/array

#get all numeric column
x_train = data1[["Gender","Age","Block","LandMark","Area","City","Pin Code","Weapon","Partner","Theft","Type of Crime"]] 
y_train = data1[["Case ID"]] 

#print(x)
#print(y)


"""
Gender_x=int(input("Take gender M(0)and F (1) : " ))
Age_x=input("Take age of criminal : " )
Block_x=int(input("Block of crime spot (0-9): " ))
LandMark_x=int(input("LandMark of crime spot(0-9) : " ))
Area_x=int(input("Area of crime spot (0-9) : " ))
City_x=int(input("City of crime spot (0-4) : " ))
PinCode_x=int(input("PinCode of crime spot (6 digit) : " ))
Weapon_x=int(input("Weapon used in crime (0-9) : " ))
Partner_x=input("Member are involve in crime : " )
Theft_x=int(input("Theft of crime (0-9) : " ))
Typeofcrime_x=int(input("Type of crime (0-3) :" ))
"""


def alo(z):
    cls= KNeighborsClassifier(n_neighbors= 5,metric='minkowski',p=2)
    cls.fit(x_train,y_train)
    #z=[[1,48,2,1,1,1,110034,1,5,2,1]]
    #z=[[Gender_x,Age_x,Block_x,LandMark_x,Area_x,City_x,PinCode_x,Weapon_x,Partner_x,Theft_x,Typeofcrime_x]]
    y_pred=cls.predict(z)
    #print(y_pred)
    y_pred=int(y_pred)
    f=data[data["Case ID"]==y_pred ]
    #u=f[["Case ID","Aadhaar No","Name","Gender","Age","Guardian","Contact","Address"]]
    u=f[["Aadhaar No","Name","Gender","Age","Guardian","Contact","Address"]]
    ind(u)
#print(u)


#split in train tand test
#x_train,x_validation,y_train,y_validation = model_selection.train_test_split(x, y, test_size=.10, random_state=7)

#print(x_train)
#print(x_validation)
#print(y_train)
#print(y_validation)
"""
L=LogisticRegression()
L.fit(x_train,y_train)
L_pred=L.predict(z)
#print(L_pred)

D=DecisionTreeClassifier()
D.fit(x_train,y_train)
D_pred=D.predict(z)
#print(D_pred)


S=SVC(gamma='auto')
S.fit(x_train,y_train)
S_pred=S.predict(z)
#print(S_pred)

G=GaussianNB()
G.fit(x_train,y_train)
G_pred=G.predict(z)
#print(G_pred)

LD=LinearDiscriminantAnalysis()
LD.fit(x_train,y_train)
LD_pred=LD.predict(y_pred)
#print(LD_pred)
"""
'''
kmeans = KMeans(n_clusters=2).fit(x_train,y_train)
centroids = kmeans.cluster_centers_

print(centroids)
print(kmeans)

plt.scatter(x_train,x_validation, c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

plt.show()
'''





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
 

#case_id=np.concatenate((L_pred, D_pred, S_pred, G_pred, LD_pred),axis=0)
#case_id=np.concatenate(( y_pred),axis=0)

#case_id=list(y_pred)
#case_id=y_pred
#print(case_id)
#caseid=most_frequent(case_id)
#print(caseid)

#print(LM_match["LandMark"])
#print(x_validation["LandMark"])
#f=data[data["Case ID"]==caseid ]
#print(f)
#v=f[["Case ID","Aadhaar No","Name","Gender","Age","Guardian","Contact","Address"]]
#v=f[["Aadhaar No","Name","Gender","Age","Guardian","Contact"]]

from tabulate import tabulate
def ind(u):
     k=["Aadhaar No","Name","Gender","Age","Guardian","Contact","Address"]
     u.set_index('Aadhaar No',inplace=True)
     print(tabulate(u,headers=k))
     import Table as t
     t.app1(u)
     #app.mainloop()

#print(type(u))

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

"""
from IPython.display import HTML
s=HTML(u.to_html(classes= 'table table-striped'))
print(s)

"""




"""
import Frontend

def Amu():
   Frontend.Lt1()
  

class Entr:
    def __init__(self):
         print('Created Client')
    def connected(self):
        print('Connected')
    def send_message(self,data2):
        print("clienrt sent '{} '".format(data2))
        




Fd=pd.DataFrame(f)

n=int(x_validation["LandMark"].values)
print(n)
M=LM_match[LM_match["LandMark"]==n]
Md=pd.DataFrame(M)

if Fd["Name"]==Md["Name"]:
    print(Fd)
"""



'''

#Build Model
# Spot Check Algorithms
models = []

models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results =[]
names = []
              
for name,model in models:
        kfold = model_selection.KFold(n_splits=10, random_state=7)
        cv_results = model_selection.cross_val_score(model, x_train, y_train, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)

'''
             
