players=[{"name":"imran","centuries":12,"half-cen":6,"wicket":8,
           "hat-trick wick":4,"batting":[120,780,340]},
         {"name":"Ronchil","centuries":15,"half-cen":7,"wicket":9,
           "hat-trick wick":6,"batting":[230,450,321]},
         {"name":"mansoor","centuries":17,"half-cen":4,"wicket":10,
           "hat-trick wick":5,"batting":[200,340,120]},
         {"name":"james","centuries":10,"half-cen":5,"wicket":13,
          "hat-trick wick":7,"batting":[320,670,560]},
         {"name":"william","centuries":17,"half-cen":8,"wicket":15,
          "hat-trick wick":6,"batting":[220,490,120]}]
   


def cricket(players):
    num=0
    for player in players:
        if(player["centuries"]>10):
            num+=1 
        print("number of players:",num)
        elif(player["hat-trick wick"])>5:
            print(player["name"]) 
        elif(player["batting"]>num):
            num=player["batting"]
    print(num)      
        
cricket(players)
#print("\n")         


