import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.preprocessing import Imputer,LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import cross_val_score
#%%
datset1=pa.read_csv("datasets/predicted_dbs/pred_one.csv")
datset2=pa.read_csv("datasets/predicted_dbs/pred_three.csv")
datset3=pa.read_csv("datasets/predicted_dbs/prod_area.csv")
datset3 = datset3[(datset3.crop != 'Maize') & (datset3.crop != 'Jute')]
#datset_district=datset.drop_duplicates('District_Name')['District_Name']
datset_crop1=datset1.drop_duplicates('crop')['crop']
datset_crop2=datset2.drop_duplicates('crop')['crop']
datset_crop3=datset3.drop_duplicates('crop')['crop']

datset3['crop'] = datset3['crop'].map({'Bajra': 'Millet', 'Ragi': 'Tea','Wheat':'Wheat','Rice':'Rice','Barley':'Barley','Jowar':'Jowar','Sugarcane':'Sugarcane','Soyabean':'Soyabean','Groundnut':'Groundnut'})
datset_crop3=datset3.drop_duplicates('crop')['crop']
#%%
def categorize(val1,val2):
    if val1>val2:
        pp=(val2/val1)
        return pp
    else:
        return 1
        

#%%
ll=[]
for i in datset3.iterrows():
    l=[]
    f1=f2=0
    crop=i[1][3]
    district=i[1][2]
    state=i[1][1]
    
    
    val1=i[1][4]
    val1_1=i[1][5]
    p1=categorize(val1,val1_1)
    
    cat2=datset2.loc[(datset2['crop'] == crop)]
    val2_1=cat2.exports.values[0]
    val2_2=cat2.imports.values[0]
    val2_3=cat2.production.values[0]

    val2_1_1=cat2.exp_mean.values[0]
    val2_2_1=cat2.imp_mean.values[0]
    val2_3_1=cat2.prod_mean.values[0]

    p2=categorize(val2_1,val2_1_1)
    p3=categorize(val2_2,val2_2_1)
    p4=categorize(val2_3,val2_3_1)
    
    cat3=datset1.loc[(datset2['crop'] == crop)]
    val3_1=cat3.Gross_Production_Value_constant_2004_2006_million_US_dollar.values[0]
    val3_2=cat3.org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar.values[0]
    p5=categorize(val3_1,val3_2)
    
    mean_final=(p1+p2+p3+p4+p5)/5
    
    l=[state,district,crop,mean_final]
    ll.append(l)

#%%
#mapping to csv
p=pa.DataFrame(ll)
p.to_csv('final_success_suggestion.csv')