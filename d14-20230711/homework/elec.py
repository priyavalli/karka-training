consumer_data={
               "consumer_name":"karthick",
               "eb_reading":[1100,1200,1350,1650,2050]
               }

details={"month":0,
         "units_consumed":0,
         "billamount":0
        }  
lista=[]                            
def calculate_electricity_bill(consumer_data):
   reading=consumer_data["eb_reading"]
   #total=0
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
   #print("billamount:",rs)
   #print("totalamount:",total) 
      detail={"month":i,"consumed data":diff,"billamount":rs}
      lista.append(detail)   
   print(lista)
   print(str(lista))

   

   #print(str(lista))
   
      #details.append(detail)
      #print(details)
      #details["month"]+=1
      #details["units_consumed"]=diff
      #details["billamount"]=rs
      #print(details) 
      
calculate_electricity_bill(consumer_data) 



          #print("units_consumed:",con1)
       #if(con1<100):
          #print("no amount to pay")
       #elif(con1>100 and con1<200):
          #rate=con1*2
          #print("billamount:",rate)
       #elif(con1>200 and con1<500):
          #rate=con1*5
       #elif(con1>500 and con1<1000):
          #rate=con1*10
          #print("billamount:",rate)
       #elif(con1>1000):
          #rate=con1*14
          #print("billamount",rate)




                       

