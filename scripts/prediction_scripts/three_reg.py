import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
from statistics import *
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import cross_val_score
#%%
datset=pa.read_csv("datasets/three.csv")
datset_crop=datset.drop_duplicates('Crop')['Crop']
#%%
def fit(x,y,crop,d):
    ppp=[]
    regressor=LinearRegression()
    for i in range(10):
        xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=i*13)
        regressor.fit(xtrain,ytrain)
        predy=regressor.predict(xtest)
        ppp.append(predy.mean())
    d[crop]=ppp
    return d
    
#%%
production={}
imports={}
exports={}
#making 3-4 regression models for each of the 10 crops
for i in datset_crop:
    dis_val=datset.loc[(datset['Crop'] == i)]
    #model 1=======production prediction
    x1=dis_val.iloc[:,6:7].values   #seed
    y1=dis_val.iloc[:,1:2].values   #production
    production=fit(x1,y1,i,production)
    print(production)
    #model2=======imports
    a=dis_val.iloc[:,3:6]
    b=dis_val.iloc[:,1:2]
    x2=b+a
    x2['Production']=b.iloc[:,0]
    for k in list(a.iloc[0:0]):
        x2[k]=a[k]
    
    y2=dis_val.iloc[:,2:3].values
    imports=(fit(x2.values,y2,i,imports))
    #model3=======exports
    a=dis_val.iloc[:,1:4]
    b=dis_val.iloc[:,6:7]
    x3=b+a
    x3['Seed']=b.iloc[:,0]
    for k in list(a.iloc[0:0]):
        x3[k]=a[k]
        
    y3=dis_val.iloc[:,4:5].values
    exports=(fit(x3.values,y3,i,exports))
    
#%%
#    finding the mean of all the entries required from the produced dictionaries
mean_prod={}
mean_imp={}
mean_exp={}
for i in datset_crop:
    mean_prod[i]=(mean(production[i]))
    mean_imp[i]=(mean(imports[i]))
    mean_exp[i]=(mean(exports[i]))
#%%
#    write these values in proper order in a csv file
lll=[]
for i in datset_crop:
    l=[]
    l.append(i)
    l.append(mean_exp[i])
    l.append(mean_imp[i])
    l.append(mean_prod[i])
    lll.append(l)
    
#%%
popo=pa.DataFrame(lll)
popo.to_csv('pred_three.csv')



