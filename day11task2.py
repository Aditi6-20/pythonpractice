x=[1,4,9,2,6,-7,-4,8,3,-2,-6]
positive=[]
negative=[]
for i in x:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
print(positive)
print(negative)
