a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
num=0
list1=[a,b,c]
for i in list1:
    if(num>i):
        num=i
print("biggest number is",i)        
    
num=0
if(num<a):
    num=a
    if(num<b):
        num=b
    if(num<c):
        num=c 
print("biggest number is",num)  

if(a>b):
    if(a>c):
        print(a,"is greater")
    else:
        print(b,"is greater")    
elif(c>a):
    if(c>b):
        print(c,"is greater")
    











           