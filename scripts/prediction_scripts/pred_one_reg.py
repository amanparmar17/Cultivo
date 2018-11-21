import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import cross_val_score
#%%
datset=pa.read_csv("datasets/one.csv")
#datset_district=datset.drop_duplicates('District_Name')['District_Name']
datset_crop=datset.drop_duplicates('Crop')['Crop']
#%%
#forming multiple linear regression model for each of the 6 attributes taking
#5/6 as independent vars and the remaining 1 as dependent vars,again and again for all the 6 vals

#p=list(datset[0:0])
#p=list(reversed(p))
ll=[]
for k in range(0,5):
    l=[]
    for j in datset_crop:
        value_crop=(datset.loc[(datset['Crop'] == j)]).iloc[:,1:]
        for i in range(0,6):
            if i<=2:
                x = value_crop.iloc[:,i+1:].values
            else:
                x = value_crop.iloc[:,0:-(6-i)].values
            y = value_crop.iloc[:, i].values
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,shuffle=True,random_state=k*23)
            regressor = LinearRegression()
            regressor.fit(x_train, y_train)
            y_pred = regressor.predict(x_test)
            l.append(y_pred.mean())
            print('{2}===={0}===={1}\n'.format(y.mean(),y_pred.mean(),j))
    ll.append(l)
    
#%%
final=np.vstack((np.array(ll[0]),np.array(ll[1]),np.array(ll[2]),np.array(ll[3]),np.array(ll[4])))
final_mean=list(np.mean(final,axis=0))


headers=list(datset[0:0])
datset_crop_list=list(datset_crop)
lll=[]
for i in range(0,len(datset_crop_list)):
    l=[]
    l.append(datset_crop_list[i])
    for j in range(0+(6*i),len(headers)-1+(6*i)):
        l.append(final_mean[j])
    lll.append(l)
    
#%%
#    writing the predicted vals to a csv file

popo=pa.DataFrame(lll)
popo.to_csv('pred_one.csv')
    