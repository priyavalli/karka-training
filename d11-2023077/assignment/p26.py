print("yee olde keychain shopper")
m1="1.Add keychains to order"
m2="2.Remove kkeychains from order"
m3="3.View keychains from order"
m4="4.Checkout"
print(m1,"\n",m2,"\n",m3,"\n",m4)
def add_keychains():
    print("ADD KEYCHAINS")
    print(m1,"\n",m2,"\n",m3,"\n",m4)
def remove_keychains():
    print("REMOVE KEYCHAINS")
    print(m1,"\n",m2,"\n",m3,"\n",m4)
def view_keychains():
    print("VIEW ORDER")
    print(m1,"\n",m2,"\n",m3,"\n",m4)
def checkout():
    print("CHECKOUT")
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
