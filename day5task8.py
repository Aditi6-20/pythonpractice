month=input('Enter a month\n')
if month=='December' or month=='January' or month=='February':
    print(f"{month} is a winter season")
elif month=='March' or month=='April' or month=='May':
    print(f"{month} is a Spring season")
elif month=='June' or month=='July' or month=='August':
    print(f"{month} is a Summer season")
elif month=='September' or month=='October' or month=='November':
    print(f"{month} is a Autum season")
else:
    print('Invalid input')