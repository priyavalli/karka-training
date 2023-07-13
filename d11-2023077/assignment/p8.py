name=input("what is your name?")
age=int(input(f"ok!{name}.how old are you?"))
if(age<16):
    print(f"you cant drive,{name}")
    print(f"you cant vote{name}")
    print(f"you cant rent a car{name}") 
elif(age<18):
    print(f"you cant vote{name}") 
    print(f"you cant rent a car{name}")
elif(age<25):
    print(f"you cant rent a car{name}")
else:
    print(f"you can do anything thats legal{name}")              