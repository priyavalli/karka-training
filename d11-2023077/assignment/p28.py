print("yee olde keychain shopper")
m1="1.Add keychains to order"
m2="2.Remove keychains from order"
m3="3.View keychains from order"
m4="4.Checkout"
print(m1,"\n",m2,"\n",m3,"\n",m4)
cur_kc=0
tot_cost=10
sales_tax=0.0825
shi_cost=5
per_cost=1
def add_keychains():
    global cur_kc
    c1=int(input(f"you have {cur_kc}keychains. how many to add?"))
    cur_kc+=c1
    print(f"you have {cur_kc} keychain")
    print("\n",m1,"\n",m2,"\n",m3,"\n",m4)
def remove_keychains():
    global cur_kc
    c2=int(input(f"you have {cur_kc} keychains. how many to remove?"))
    cur_kc-=c2
    print(f"you now have {cur_kc}keychains")
    print(m1,"\n",m2,"\n",m3,"\n",m4)
def view_keychains():
    global cur_kc
    global tot_cost
    global sales_tax
    global shi_cost
    global per_cost  
    print(f"\n you have {cur_kc} keychains")
    print(f"price per keychain{per_cost}")
    print(f"shipping cost:"cur_kc*shi_cost)
    print("keychains cost $10 each")
    print(f"total cost is{cur_kc*tot_cost}")
    gst=(cur_kc*tot_cost)
    print(f"{cur_kc*per_cost+shi_cost}")
    print(f"")
    print("\n",m1,"\n",m2,"\n",m3,"\n",m4)
def checkout():
    global cur_kc
    global tot_cost
    global sales_tax
    global shi_cost
    global per_cost 
    print("CHECKOUT")
    c3=input("what is your name?")
    print(f"you have {cur_kc} keychains")
    print("keychains cost $10 each")
    print(f"total cost is {cur_kc*tot_cost}")
    print(f"thanks for ordering,{c3}")
for i in range(5):
    print(i)
    choice=int(input("enter your choice"))
    if(choice==1):
        add_keychains()
    if(choice==2):
        remove_keychains()
    if(choice==3):
        view_keychains()
    if(choice==4):
        checkout()
        break  