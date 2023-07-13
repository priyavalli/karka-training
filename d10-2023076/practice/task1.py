marks=[96,72,80,67,82]
tot_marks=0
for mark in marks:
    print("before",tot_marks)
    tot_marks=tot_marks+mark
    print("after",tot_marks)

    enum_mark=enumerate(marks)
    print(type(enum_mark))
for i,marks in enum_mark:
    print("Entering the process of item:"+str(i))
    print("before sum",tot_marks)
    tot_marks=tot_marks+marks
    print("After sum",tot_marks)
    print("existing the process of item:"+str(i))
    print("\n")
