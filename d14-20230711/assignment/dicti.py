friends=[{"name":"valli","age":21,"place":"krishnan kovil"},
         {"name":"subin","age":25,"place":"parvathipuram"},
         {"name":"varathan","age":21,"place":"saamithoapu"},
         {"name":"robin","age":22,"place":"tvl"},
         {"name":"sreeram","age":23,"place":"thamaraikulam"},
         {"name":"supriya","age":21,"place":"ganesapuram"},
         {"name":"vajeeha","age":21,"place":"thittuvizhai"}]       
          


def fn(friends):
    for friend in friends:
        print("iam",friend["name"],"iam from",friend["place"],"and iam",friend["age"],"years old")   
        #print("\n")
        if(friend["age"]>21):
            print("name:",friend["name"],"\nplace:",friend["place"])
fn(friends)            
 




#def age(friends):
    #for friend in friends:
        #if(friend["age"]>21):
            #print("name:",friend["name"],"\nplace:",friend["place"])
#age(friends)