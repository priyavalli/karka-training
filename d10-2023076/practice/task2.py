marks=[96,72,80,67,82]
tot_mark=0
for mark in marks:
    
enum_mark=enumerate(marks)
print(type(enum_mark))
for i,mark in enum_mark:
    print("Entering iteration process of item:"str(i))
    print("before sum")