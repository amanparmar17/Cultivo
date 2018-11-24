import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import cross_val_score
#%%
datset=pa.read_csv('district_wise_crop_success.csv')
datset_state=datset.drop_duplicates('state')['state']
#%%
ll=[]
for i in datset_state:
    distinct_state_crop=datset.loc[(datset['state'] == i)].drop_duplicates('crop')['crop']
    for j in distinct_state_crop:
        l=[]
        crop_vals=datset.loc[(datset['state'] == i) & (datset['crop'] == j)]['success_rate']
        mean_success=crop_vals.mean()
        l=[i,j,mean_success]
        ll.append(l)

#%%
p=pa.DataFrame(ll)
p.to_csv('state_wise_crop_success.csv')