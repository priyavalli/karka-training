weight=int(input("enter the weight in kg:"))
height=float(input("enter the weight in m:"))
tot_BMI=weight/(height*height)
import p7
p7.BMI_calc(height,weight)
#height=float(input("Enter the height in m:"))
#weight=int(input("enter the weight in kg:"))
#tot_BMI=weigh/(heigh*heigh)

if(tot_BMI<18.5):
    print("BMI Category: under weight")
if(tot_BMI>=18.5 and tot_BMI<=24.9):
    print("BMI Category: normal weight")
if(tot_BMI>25.0 and tot_BMI<=29.9):
    print("BMI Categoty: over weight")
if(tot_BMI>=30.0):
    print("BMI Category: obese")           