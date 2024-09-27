year=int(input('Enter a year\n'))
if (year%4==0 and year%100!=0) or ():
    print(f"{year} is a leap year ")
else:
    print(f'{year} is not a leap year')
