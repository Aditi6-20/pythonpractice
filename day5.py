balance=int(input("Enter your balance\n"))
age=int(input("Enter your age\n"))
if age>=20 and age<30 :
    print(f"your current balance {balance+10000}")
elif age>=35 and age<45:
    print(f"your current balance {balance+15000}")
elif age>=50 and age<70:
    print(f"your current balance {balance+5000}")
else:
    print("you are not elegible Scheme!")
