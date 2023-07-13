mass=int(input("please enter your current earth weight"))
print("I have information about the following planets")
print("\t 1.venus \t 2.Mars \t 3.Jupiter")
print("\t 4.Satrun \t 5.Urenus \t 6.Neptune")
planet=int(input("which planet are you visiting:"))
if(planet==1):
    a=mass*0.78
    print("your weight would be",a,"pounds on that planet")
elif(planet==2):
    b=mass*0.39
    print("your weight would be",b,"pounds on that planet") 
elif(planet==3):
    c=mass*2.65
    print("your weight would be",c,"pounds on that planet")
elif(planet==4):
    d=mass*1.17
    print("your weight would be",d,"pounds on that planet")
elif(planet==5):
    e=mass*1.05
    print("Your weight would be",e,"pounds on that planet")
elif(planet==6):
    f=mass*1.23
    print("your weight would be",f,"pounds on that planet") 
else:
    print("invalid")                     

