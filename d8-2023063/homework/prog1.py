a=input("enter the first integer:")
b=input("enter the operator:")
c=input("enter the second integer:")
a_int=int(a)
c_int=int(c)

def calc_int(a_int,b,c_int):
    if(b== '+'):
        return a_int+c_int
    if(b=='-'):
        return a_int-c_int
    if(b=='*'):
        return a_int*c_int
    if(b=='/'):
        return a_int/c_int   
    if(b=='%'):
        return a_int%c_int         
     
answer=calc_int(a_int,b,c_int)
print(answer)          

