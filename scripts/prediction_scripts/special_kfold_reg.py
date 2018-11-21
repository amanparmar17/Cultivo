#let the number of divisions be 5
datset=datset_crop
start=0
number=5
i=1
l=[]
while(len(datset)>0):
    if len(datset)>number:
        dat=datset[start:(number*i)]
        start=(number*i)
        l.append(dat)
        datset=datset[start:]
        i+=1
        print(i)
    else:
        dat=datset[start:]
        l.append(dat)
        print('done')
    #%%