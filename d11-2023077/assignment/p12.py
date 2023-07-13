quiz=input("Are you ready for the quiz?")  
n=0
if(quiz=="yes"):
    print("Ok here it is")
    q1=int(input("\t1.what is the capital of alaska?\n\t 1)melbourence\n\t 2)anchorage\n\t 3)Juneau\n>"))
    if(q1==3):
        print("That's right")
        n=n+1
    else:
        print(" you are wrong")    
    q2=int(input("\t2.can you store the value cat in a variable of type int?\n\t111)yes\n\t2)No\n>"))
    if(q2==1):
        print("Sorry cat is a string ints can only store numbers") 
    else:
        print("you are right")
        n=n+1
    q3=int(input("\t3.what is the resullt of 9+6/3?\n 1)5\n 2)11 \n 3)15/3?\n>"))
    if(q3==2):
        print("you are correct")
        n=n+1 
    else:
        print("you are wrong")
        print("overall you got",n,"out of 3\n Thanks for playing" )

    



