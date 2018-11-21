import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import cross_val_score
#%%
datset=pa.read_csv("datasets/three.csv")
#datset_district=datset.drop_duplicates('District_Name')['District_Name']
datset_crop=datset.drop_duplicates('Crop')['Crop']
#%%
headers=list(datset[0:0])[1:]
mea=[]
for i in datset_crop:
    a={}
    a['crop']=i
    value=(datset.loc[(datset['Crop'] == i)])
    for j in headers:
        mean_1=(value[j]).mean()
        a[j]=mean_1
    mea.append(a)
        
        
    