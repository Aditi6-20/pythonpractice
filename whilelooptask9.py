num=[12,56,-9,5,7,3,2]
smallest = num[0]
i=1
while i<len(num):
    if num[i] < 0:
        smallest = num[i]
    i+=1

print('The smallest element is :',smallest)