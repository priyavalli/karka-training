name=input("Hey,unnatha What's your name (sorry I keep forgetting)?")
age=int(input(f"ok,{name},how old are you?"))
if(age<16):
    print("you can't drive")
elif(age==16 and age==17):
    print("You can drive but not vote")
elif(age>=18 and age<=24):
    print("you can vote but not rent a car")
elif(age>=25):
    print("you can do pretty much anything")            