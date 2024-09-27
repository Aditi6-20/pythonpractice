yr=int(input('Enter the No. of year of service\n'))
sal=25000
sal1=25000+10000
sal2=25000+15000
sal3=25000+20000
if yr>=1 and yr<=5:
    print(f"Your monthly sal ={sal}\nBonus=10000\nYour total sal={sal1}  ")
elif yr>=6 and  yr<=10:
    print(f"Your monthly sal ={sal}\nBonus=15000\nYour total sal= {sal2} ")
elif yr>=11 and  yr<=15:
    print(f"Your monthly sal ={sal}\nBonus=20000\nYour total sal= {sal3} ")