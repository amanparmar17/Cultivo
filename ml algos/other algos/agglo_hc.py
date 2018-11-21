import pandas as pa
import numpy as np
import matplotlib.pyplot as plt  

datset=pa.read_csv("Mall_Customers.csv")
x= datset.ix[:,3:5].values

import scipy.cluster.hierarchy as sch
dendogram=sch.dendrogram(sch.linkage(x,method="ward"))
plt.title("dendogram")
plt.xlabel('customers')
plt.ylabel('eucledian distance')
plt.show() 

#%%

from sklearn.cluster import AgglomerativeClustering
obj=AgglomerativeClustering(n_clusters=5,affinity="euclidean",linkage="ward")
ypred=obj.fit_predict(x)
#%%
plt.scatter(x[ypred==0,0],x[ypred==0,1],s=100,c="red",label="cluster 1")
plt.scatter(x[ypred==1,0],x[ypred==1,1],s=100,c="blue",label="cluster 2")
plt.scatter(x[ypred==2,0],x[ypred==2,1],s=100,c="green",label="cluster 3")
plt.scatter(x[ypred==3,0],x[ypred==3,1],s=100,c="cyan",label="cluster 4")
plt.scatter(x[ypred==4,0],x[ypred==4,1],s=100,c="magenta",label="cluster 5")

plt.xlabel("income")
plt.ylabel("credit score")
plt.legend()
plt.show()
