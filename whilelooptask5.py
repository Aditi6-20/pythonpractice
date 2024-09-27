s=input('Enter a String')
s.lower()
count=0
for i in s:
    if s[i]=='c':
        count+=1
    print(count)