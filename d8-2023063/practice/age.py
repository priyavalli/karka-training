a=input("enter your age:")
int_a=int(a)


def is_eligible(int_a):
    if(int_a<18):
        return "you are noteligible to vote"
    else:
        return "you are eligible to vote"  


int_age=is_eligible(int_a)
print(int_age)




