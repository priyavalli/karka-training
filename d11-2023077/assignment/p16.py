gender=input("What is your gender:")
f_name=input("First Name:")
l_name=input("Last Name:")
name=f_name+l_name
age=int(input("Age:"))
if(gender=="female" and age>=20):
    i1=input("Are you married?")
    if(i1=="yes"):
        print(f"Then I shall call you Mrs.{name}")
    else:
        print(f"Then I shall call you Ms.{name}")
elif(gender=="female" and age<20):
    print(f_name,l_name)        
elif(gender=="male" and age>=20):
    print(f"Then I shall call you Mr.{name}") 
else:
    print(f_name,l_name)
           

                   

