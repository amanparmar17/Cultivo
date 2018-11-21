import numpy as np
import pandas as pa
import matplotlib.pyplot as plt

#%%
#read the datset
dataset_main= pa.read_csv('datasets/apy.csv')
#%%
#filter the datset,,,remove areas where area is<200
b= datset[(datset['Area']>200)]
#%%
#adding a new col of prod/area
b['prod_area']=b['Production']/b['Area']
#%%
#handling the null prod/area fields
b[b['prod_area'].isnull()]=0
    
#%%
#selecting the major 10 states!
states=[
        'Uttar Pradesh',
        'Madhya Pradesh',
        'Haryana',
        'Bihar',
        'Andhra Pradesh',
        'Maharashtra',
        'West Bengal',
        'Gujarat',
        'Punjab',
        'Rajasthan',
        'Karnataka',
        'Tamil Nadu'
        ]

c=b[b.State_Name.isin(states)]

#%%
#finding the total sum of prod_area ----- state wise to calculate the normalised prod_area state_wise
l={}
for i in states:
    l[i]=c[c.State_Name==(i)]['prod_area'].sum()
#%%
#initialising the final col as nan
c['state_norm_val']=np.nan
#%%
#state wise normalisation of prod_area
for i in states:
    c.state_norm_val[c['State_Name']==i] = (c[c['State_Name']==i]['prod_area']/l[i])
    
#%%
#writing the final dataframe to csv
c.to_csv('norm_data_apy.csv')
#%%
#filtering the crops
crops=['rice','wheat','sugarcane','cotton','groundnut','tea','coffee','bajra','soyabean','maize','barley','mustard','peas','ragi','jowar','coconut','jute','rubber']

#%%
#capitalising each crop
for i in range(0,len(crops)):
    crops[i]=crops[i].capitalize()
    #%%
g=datset[datset.Crop.isin(crops)]