import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import cross_val_score
#%%
datset=pa.read_csv("datasets/crop_final_details_apy.csv")
datset_district=datset.drop_duplicates('District_Name')['District_Name']
datset_crop=datset.drop_duplicates('Crop')['Crop']
#%%
#predicting production/area from area for each of the crop in a particular district
#thus making about 390*11 regression models and saving the final values in a seperate file

regressor=LinearRegression()

we=[]

for i in datset_district:
    value_district=datset.loc[(datset['District_Name'] == i)].drop_duplicates('Crop')
    for j in value_district['Crop']:
        x= value_district.ix[:,5:6].values
        y= value_district.ix[:,7:8].values
        xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=0)
        regressor.fit(xtrain,ytrain)
        accuracies=cross_val_score(estimator=regressor,X=xtrain,y=ytrain,cv=2)
        q=accuracies.mean()
        print('for Crop {0} in District {1} the mean accuracy is {2}'.format(j,i,q))
        we.append(q)

        
        #%%
regressor=LinearRegression()
value_district=datset.loc[(datset['District_Name'] == 'ANANTAPUR')].drop_duplicates('Crop')
#for j in value_district['Crop']:
www=datset.loc[(datset['Crop'] == 'Rice') & (datset['District_Name'] == 'ANANTAPUR')]
try:
    x= www.iloc[:,5:6].values
    y= www.iloc[:,7:8].values
    xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=0)
    regressor.fit(xtrain,ytrain)
    predy=regressor.predict(xtest)
except ValueError:
    print(www)

#%%
regressor=LinearRegression()
ppp=[]
#value_district=datset.loc[(datset['District_Name'] == 'ANANTAPUR')].drop_duplicates('Crop')
for i in datset_district:
    value_district=datset.loc[(datset['District_Name'] == i)].drop_duplicates('Crop')
    for j in value_district['Crop']:
        www=datset.loc[(datset['Crop'] == j) & (datset['District_Name'] == i)]
        try:
            x= www.iloc[:,5:6].values
            y= www.iloc[:,7:8].values
            xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=0)
            regressor.fit(xtrain,ytrain)
            predy=regressor.predict(xtest)
    #        accuracies=cross_val_score(estimator=regressor,X=xtrain,y=ytrain,cv=6)
    #        q=accuracies.mean()
    #        print(q)
            pred_min=predy.mean()-0.2
            pred_max=predy.mean()+0.2
            pred_mean=(pred_max+pred_min)/2
            state=list(www.loc[(www['District_Name'] == i)].drop_duplicates('State_Name')['State_Name'])
            l=[state[0],i,j,www['prod_area'].mean(),pred_mean]
            ppp.append(l)
            print(l)
        except ValueError:
            print(www)
            #%%
#ddd={'state':ppp[0],'district':ppp[1],'crop':ppp[2],'org_val':ppp[3],'pred_val':ppp[4]}
p=pa.DataFrame(data=ppp)
p.to_csv('prod_area.csv')
        
    