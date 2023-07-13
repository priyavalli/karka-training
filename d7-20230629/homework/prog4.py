a=input("enter the amount of item1=")
b=input("enter the amount of item2=")
c=input("enter the amount of item3=")
d=input("enter the amount of item4=")
int_a=int(a)
int_b=int(b)
int_c=int(c)
int_d=int(d)
total=int_a+int_b+int_c+int_d
if total>=500 and total<=1000:
    print("you have owned a silver token")
if total>1000:
    print("you have owned a gold tokens")    

