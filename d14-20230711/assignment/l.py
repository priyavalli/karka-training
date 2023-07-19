names=[
       {
              "name":"valli",
              "place":"ngl",
              "hobby":"meme creating",
              "sslc":{"Tamil":89,"English":78,"Maths":99,"Science":89,"SocialScience":90}
       },
       { 
              "name":"supriya",
              "place":"gpm",
              "hobby":"movies",
              "sslc":{"Tamil":67,"English":89,"Maths":89,"Science":67,"SocialScience":89}
       },
       {
              "name":"vajeega",
              "place":"tvl",
              "hobby":"music",
              "sslc":{"Tamil":89,"English":78,"Maths":56,"Science":89,"SocialScience":67}
       }
       ]
       
#print(names[3]["hobbies"])
#a=names[3]["hobbies"]
#for i in a:
    #print(i)
for name in names:
       mark1=name["sslc"]["Tamil"]
       mark2=name["sslc"]["English"]
       mark3=name["sslc"]["Maths"]
       mark4=name["sslc"]["Science"]
       mark5=name["sslc"]["SocialScience"]
       tot=mark1+mark2+mark3+mark4+mark5
       print(tot) 

       percentage=tot/5
       print(percentage)
       if(percentage>90):
              print("eligible for maths biology")
       elif(percentage>80):
              print("eligible for computer science") 
       elif(percentage>75 and name["sslc"]["Maths"]>98):
              print("eligible for maths bio")
       elif(percentage>70 and name["sslc"]["Maths"]>=98):
              print("eligible for maths computer")  
       else:
              print("not eligible")                        



