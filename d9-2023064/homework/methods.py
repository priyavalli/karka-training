amount="string is a collection of charecters"
amount2="my name is JOHN"
str1="banana123"
str2="12789"
str3="    "
print(amount.title())
print(amount.capitalize())
print(amount2.casefold())
print(amount.count('s'))
print(amount.center(43))
print(amount2.center(29,'*'))
print(amount.endswith("s"))
print(amount2.endswith("n"))
print(amount.find("is"))
print(amount2.find("name"))

amount3="my name is {},iam {}".format("john",89)
print(amount3)

amount4={'x':'karthick','y':'27'}
print("{x} is {y} years old".format_map(amount4))

print(amount.index("is"))

print(str1.isalnum())
print(str1.isalpha())
#print(str1.isascii())
#print(str2.isdecimal())
print(str2.isdigit())
print(amount2.islower())
print(amount.isupper())
print(str2.isnumeric())
#print(str2.printable())
print(str3.isspace())
print(amount.istitle())
#print(amount2.join("k"))
#print(amount.ljust(9))
print(amount2.lower())
#print(amount.lstrip())
