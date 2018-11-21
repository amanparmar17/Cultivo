import numpy as np
import pandas as pa
import matplotlib.pyplot as plt
from minor import *
#%%
datset=pa.read_csv('datasets/norm_data_apy.csv')
#%%
datset['lat']=np.nan
datset['long']=np.nan
#%%
#drop duplicates
e=datset.drop_duplicates('District_Name')
#%%
def red(df,index):
    df=df.truncate(index)
    return df
#%%
for i in e['District_Name']:
    try:
        if ' ' in i:
            place=i.replace(' ','+')
        elif i == 'VISAKHAPATANAM':
            place='VISAKHAPATNAM'
        else:
            place=i
        coordinates=geocoding(place)
        print('coordinates of {0}: {1}'.format(i,coordinates))
        datset.lat[datset['District_Name']==i] = coordinates[0]
        datset.long[datset['District_Name']==i] = coordinates[1]
    except IndexError:
        fault_index=e.loc[e['District_Name']==i].index[0]
        e=red(e,fault_index)

#%%
#        distinct crops
datset.to_csv('final_apy.csv')
#%%
f=datset.drop_duplicates('Crop')
f=f['Crop']
f.to_csv('distinct_crops_apy.csv')

