import pandas as pa
import csv
import statistics as stat
#%%
dataset=pa.read_csv('old_datasets/value_data.csv')
#%%
#selecting the unique field value from the first column
e=dataset.drop_duplicates('Element')['Element']
#%%
#getting unique crops from the dataset
crops=dataset.drop_duplicates('Item')['Item']
crops=list(crops)
#%%
#add crop name to the start of the headings i.e the first column name
e=list(e)
r=['Crop']
r.extend(e)
f=[]
f.append(r)

with open('one.csv','w') as ff:
    writer=csv.writer(ff)
    writer.writerows(f)
#%%

def insert(l1,row):
    for k in range(0,len(row)):
        l1[k].append(list(row['Value'])[k])
    return l1
e=dataset.drop_duplicates('Element')['Element']

name='one.csv'
with open(name,'a') as ff:
    for i in crops:
        l1=[[i] for _ in range(10)]
        for j in e:
            row=dataset.loc[(dataset['Element']==j) & (dataset['Item']==i)]
            l1=insert(l1,row)
        writer=csv.writer(ff)
        writer.writerows(l1)
