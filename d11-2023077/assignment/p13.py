print("TWO QUESTIONS")
print("Think of an object,and i'll try to guess it")
q1=input("q1) It is animal,vegetables, or mineral?\n")
q2=input("q2) It is bigger than a breadbox?\n")
if(q1=="animal"):
    if(q2=="yes"):
        print("my guess is that you are thinking of a mouse")
        print("I would ask you if I'm right,but I dont care")
    else:
        print("my guess is that you are thinking of a squiril")
        print("I would ask you if i'm right,bit i dont care")    
elif(q1=="vegetables"):
    if(q2=="yes"):
        print("my guess is that you are thinking of a water melon")
        print("I would ask you if i'm right,but i dont care")
    else:    
        print("my guess is that you are thinking of a carrot")
        print("i would ask you if i'm right,but i dont care")
elif(q1=="mineral"):
    if(q2=="yes"):
        print("my guess is that you are thinging of a camero")
        print("i would ask you if i'm right,but i  dont care")
    else:
        print("my guessis that you are thinking of a paperclip")
        print("i would ask you if i'm right,but i dont care")    
       

