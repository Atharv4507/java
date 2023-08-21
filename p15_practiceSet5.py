# 1st probleam
# n1 = int(input("Enter num1: "))
# n2 = int(input("Enter num2: "))
# n3 = int(input("Enter num3: "))
# n4 = int(input("Enter num4: "))

# if(n1 > n4):
#     f1 = n1
# else:
#     f1 = n4

# if(n2 > n3):
#     f2 = n2
# else:
#     f2 = n3

# if(f1 > f2):
#     print(str(f1) + " is gratest")
# else:
#     print(str(f2) + " is gratest")


# 2nd probleam
# sub1 = int(input("Enter sub1 marks: "))
# sub2 = int(input("Enter sub2 marks: "))
# sub3 = int(input("Enter sub3 marks: "))
# if(sub1 < 33 or sub2 < 33 or sub3 < 33):
#     print("You are fail cuz you have less than 33% in one of subject")
# elif((sub1+sub2+sub3)/3 < 40):
#     print("you are fail due to total percentage less than 40%")
# else:
#     print("Congratulation! you passed the exam")


# 3rd probleam
text = input("Enter the text\n")
spam = False
if("Make alot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("get now" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam!")
else:
    print("this text is not spam")