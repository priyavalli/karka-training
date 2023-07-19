#Name="valli"
#dict_name={"name":Name}
#print(dict_name)

item_list=[
          {'name':'banana','category':'fruits'},
          {'name':'apple','category':'fruits'},
          {'name':'brocoli','category':'vegetable'},
          {'name':'carrot','category':'vegetable'}
         ]

#fruits=[]
#vegetables=[]
a=fruit
b=
for i in item_list:
    if(i['category']=='fruits'):
        fruits.append(i['name'])
    elif(i['category']=='vegetable'):
        vegetables.append(i['name'])  
print("fruit:",fruits) 
print("vegetable:",vegetables)  

category={"fruit":fruits,
           "vegetable":vegetables}
print(category)

