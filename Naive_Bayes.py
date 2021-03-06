#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
df=pd.read_csv('Social_Network_Ads.csv')
X=df.iloc[:,[2,3]].values
y=df.iloc[:,4].values

#Splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

#fitting the classifier to the training set
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier .fit(X_train,y_train)

#predicting the test set result
y_pred=classifier.predict(X_test)

#making confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_pred)
print(cm)

#Visualising the training set result
from matplotlib.colors import ListedColormap
X_set,y_set=X_train,y_train
X1,X2=np.meshgrid(np.arange(X_set[:,0].min()-1,X_set[:,0].max()+1,0.01),np.arange(X_set[:,1].min()-1,X_set[:,1].max()+1,0.01))
Z=classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape)
plt.contour(X1,X2,Z,cmap=ListedColormap('red','green'))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==i,0],X_set[y_set==i,1],cmap=ListedColormap(('red','green'))(i),label=j)
plt.title("Naive Bayes(trainig set)")
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()

#Visualising the test set result
from matplotlib.colors import ListedColormap
X_set,y_set=X_test,y_test
X1,X2=np.meshgrid(np.arange(X_set[:,0].min()-1,X_set[:,0].max()+1,0.01),np.arange(X_set[:,1].min()-1,X_set[:,1].max()+1,0.01))
Z=classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape)
plt.contour(X1,X2,Z,cmap=ListedColormap('red','green'))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==i,0],X_set[y_set==i,1],cmap=ListedColormap(('red','green'))(i),label=j)
plt.title("Naive Bayes(test set)")
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()



















