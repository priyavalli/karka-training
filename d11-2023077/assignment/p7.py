height=float(input("your height in m: "))
weight=int(input("your weight in kg:"))
def BMI_calc(height,weight):
    tot_BMI=weight/(height*height)
    return tot_BMI

res=BMI_calc(height,weight)
print("your total BMI",res)
   