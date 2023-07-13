# area of triangle
#sidea=int(input("Enter the a value:"))
#sideb=int(input("Enter the b value:"))
#sidec=int(input("enter the c value:"))
#s=int((sidea+sideb+sidec)/2)
def area_tr():
    sidea=int(input("Enter the a value:"))
    sideb=int(input("Enter the b value:"))
    sidec=int(input("enter the c value:"))
    s=int((sidea+sideb+sidec)/2)
    return (s*(s-sidea)*(s-sideb)*(s-sidec))**2
     
#area of square
#a=int(input("enter the a value:"))
def area_sq():
    a=int(input("enter the a value:"))
    return a*a
  


#area of rectangle
#en=int(input("enter the l value:"))
#wid=int(input("enter the w value:"))
def area_rec():
    len=int(input("enter the l value:"))
    wid=int(input("enter the w value:"))
    return len*wid
# result=area_rec(len,wid)
# print(result)  

# #area of circle
#radius=int(input("enter the r value:"))
def area_cir():
    radius=int(input("enter the r value:"))
    return 3.14*radius*radius
# result=area_cir(radius) 
# print(result)   

# #area of trapizum
#base1=int(input("enter the a value:"))
#base2=int(input("enter the b value:"))
#height=int(input("enter the h value:"))
def area_trap():
    base1=int(input("enter the a value:"))
    base2=int(input("enter the b value:"))
    height=int(input("enter the h value:"))
    a1=base1+base2
    return 0.5*a1*height
# result=area_trap(base1,base2,height)
# print(result)  


i2=input("enter choice:")
if(i2=="1"):
    print(area_tr())
if(i2=="2"):
    print(area_sq())
if(i2=="3"):
    print(area_rec())
if(i2=="4"):
    print(area_cir())   
if(i2=="5"):
    print(area_trap())             



