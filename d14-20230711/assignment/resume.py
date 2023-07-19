my_resume={
           "name":"valli",
           "email":"abc@gmail.com",
           "mobile no":9994445264,
           "softskill":"creative thinking",
           "hardskill":"typing",
           "educational-qualification":
            [{
            "level":"sslc",
            "per":"88%",
            "POY":2018,
            "school":"St.Josephs convent HR.SEC school"
            },
            {
            "level":"plus2",
            "per":"78%",
            "POY":2020,
            "school":"St.Joseph's convent HR.SEC school"
            },
            {
             "level":"degree",
             "per":"75%",
             "POY":2023,
             "college":"WCC"
            }],
           "projects":"android app develepmentusing kotlin",
           "experience":[{"company name":"scope india",
                        "role":"backend develepor",
                        "duration":1
                         },
                         {
                         "company name":"inbox info solutions",
                         "role":"backenddeveloper",
                         "duration":2
                         }],
           "hobbies":["listening music","meme creating","drawing"],
           "personal-details":{"Fathername":"T.senthil ganesh",
                               "Fathersocuupation":"coolie",
                               "languages known":["tamil","english"],
                               "DOB":"19.4.2003",
                               "Gender":"female",
                               "address":{"door no":6,
                                         "street name":"vanigar street",
                                         "place":"krishnan koil",
                                         "distrit":"kanyakumari","pin":629001},
                               "Martial status":"single"}
            }          
print(my_resume)
print("\n")
print(my_resume.items())
print("\n")
print(my_resume.values())
print("\n")
print(my_resume.keys())
print("\n")
print(my_resume["name"])
print("\n")

#print(my_resume["educational-qualification"])
for i in my_resume['personal-details']:
    #print(i)
    #print(my_resume[i])
    print(f"{i}:{my_resume['personal-details'][i]}")
if(i==['address']):
    for j in my_resume['personal-details']['address']:
            print(j)
#for j in my_resume['educational-qualification']:
    #print(j) 
    #print("\n")
    #print(j["level"])







                                                                                                       

    

    


