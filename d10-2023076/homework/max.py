#numbers=[1,100,300,4]
#num=0
#for a in numbers:
 #if(num>a):
     #print("largest number is:",num)
 ##num=a

     
numbers=[1,100,300,4]
num=0
def calc_num(numbers,num):
    for a in numbers:
        if(a>num):
            num=a
    return num
x=calc_num(numbers,num) 
print(x)           
                       




