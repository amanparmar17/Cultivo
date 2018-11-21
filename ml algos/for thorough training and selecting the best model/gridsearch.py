import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
#%%
datset=pa.read_csv("Social_Network_Ads.csv")
x= datset.ix[:,2:4].values
y= datset.ix[:,-1].values
#%%

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=0)
#%%
from sklearn.preprocessing import StandardScaler
scx=StandardScaler()
xtrain=scx.fit_transform(xtrain)
xtest=scx.transform(xtest)
#%%
from sklearn.svm import SVC
classifier=SVC(kernel="rbf",random_state=0)
classifier.fit(xtrain,ytrain)
#%% 
#ypred=classifier.predict(xtest)
##%%
#from sklearn.metrics import confusion_matrix
#cm=confusion_matrix(ytest,ypred)

#%%applying k-fold cross validation
from sklearn.model_selection import cross_val_score  #method imported
accuracies=cross_val_score(estimator=classifier,X=xtrain,y=ytrain,cv=10)
accuracies.mean()

#%% applying the gris search for finding the best suitable combination of the optimal model and parameters
from sklearn.model_selection import GridSearchCV
parameters=[{'C':[1,10,100,1000],'kernel':['linear']},
             {'C':[1,10,100,1000],'kernel':['rbf'],'gamma':[0.5,0.1,0.01,0.001]}
            ]
gs=GridSearchCV(estimator=classifier,
                param_grid=parameters,
                scoring='accuracy',
                cv=10,
                n_jobs=-1
                )
gs=gs.fit(xtrain,ytrain)
best_accuracy=gs.best_score_
best_params=gs.best_params_

#%% visualisation
from matplotlib.colors import ListedColormap
xset,yset=xtrain,ytrain 
x1,x2= np.meshgrid(np.arange(start=xset.min()-1,stop=xset.max()+1,step=0.01),
                   np.arange(start=xset.min()-1,stop=xset.max()+1,step=0.01))

plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
             alpha=0.75,cmap=ListedColormap(('red','green')))
             
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())

for i,j in enumerate(np.unique(yset)):
    plt.scatter(xset[yset==j,0],xset[yset==j,1],
                c=ListedColormap(('red','green'))(i),label=j)
plt.legend()
plt.show()
