#a=input("covert format:")
consumer_data={
               "consumer_name":"riya",
               "eb_reading":[1100,1200,1350,1650,2050]
               }

details={"month":0,
         "units_consumed":0,
         "billamount":0
        }  
lista=[]
import json                            
def calculate_electricity_bill(consumer_data):
   reading=consumer_data["eb_reading"]
   for i in range(1,len(reading)):
      total=0
      rs=0
      diff=reading[i]-reading[i-1]
      #print(f"month:{i}\nunits consumed:{diff}")
   
      if(diff<100):
         print("no amount to pay")
      elif(diff>=100 and diff<200):
         rs=diff*2 
         #print("billamount:",rs)
      elif(diff>200 and diff<500):
         rs=diff*5
         #print("billamount:",rs)
      elif(diff>500 and diff<1000):
         rs=diff*10
         #print("billamount:",rs)
      elif(diff>1000):
         rs=diff*15
      total=total+rs   
      detail={"month":i,"consumed data":diff,"billamount":rs}
      lista.append(detail) 
   #print(lista)   
   return str(lista)
a=calculate_electricity_bill(consumer_data)
str_a=str(a)

#print(calculate_electricity_bill(consumer_data))
b=input("enter the convert format:")
f=open("/home/valli/karka/d14-20230711/practice/valli.txt","w")
f.write(str_a)
if(b.upper()=="DICT"):
   print(a)
if(b.upper()=="JSON"):
   js=json.dumps(str_a)
   print(js)
f.close()   



f=open("/home/valli/karka/d14-20230711/practice/valli.txt","r")
#choice=input("enter the convert format:")
#if(choice.upper()=="DICT"):
#print()




   

   #print(str(lista))
   
      #details.append(detail)
      #print(details)
      #details["month"]+=1
      #details["units_consumed"]=diff
      #details["billamount"]=rs
      #print(details) 
      
calculate_electricity_bill(consumer_data) 


