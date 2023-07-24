month_gold_rate=[{"month":"jan","gold rate":2000},
                 {"month":"feb","gold rate":3400},
                 {"month":"march","gold rate":8000},
                 {"month":"april","gold rate":9000}]
mini=month_gold_rate[0]["gold rate"]
maxi=0
min_month=month_gold_rate[0]["month"]
max_month=0
for i in month_gold_rate:
    if(i["gold rate"]<mini):
        mini=i["gold rate"]
        min_month=i["month"]
    elif(i["gold rate"]>maxi):
        maxi=i["gold rate"] 
        max_month=i["month"]           
print("lowest gold rate",mini)
print("highest gold rate",maxi)
print("lowest rate month",min_month)
print("highest rate month",max_month)


        



                                      