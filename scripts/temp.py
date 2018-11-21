import numpy as np
import pandas as pa
import matplotlib.pyplot as plt
from minor import *
#from datset_create import filtering
#%%
datset=pa.read_csv('datasets/old_datasets/final_apy.csv',header=0)
#%%
crops=['rice','wheat','sugarcane','cotton','groundnut','tea','coffee','bajra','soyabean','maize','barley','mustard','peas','ragi','jowar','coconut','jute','rubber']
for i in range(0,len(crops)):
    crops[i]=crops[i].capitalize()
    #%%
g=datset[datset.Crop.isin(crops)]
#%%
#saving the dataset
g.to_csv('crop_final_details_apy.csv')
#dat_sample=filtering(datset)