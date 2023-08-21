a = 45
if(a > 3):
    print("The value of a is greater than 3")
elif(a > 7):
    print("The value of a is greater than 7")
else:
    print("The value is not greater than 3 or 7")

b = None
if(b is None):
    print("Yes")
else:
    print("No")


c = [45, 65, 78]
# if(45 in c):
#     True
# else:
#     False    
print(45 in c)