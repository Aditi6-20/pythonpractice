cha=input('Enter any character\n')
cha=cha.lower()
i=0
count=0
while i<len(cha):
  if cha[i]=='a'or cha[i]=='e'or cha[i]=='i'or cha[i]=='o' or cha[i]=='u':
    count+=1
  i+=1
print(count)