# ## 1st que
# def num(n1, n2, n3):
#     if(n1 > n2 & n1 > n3):
#         return n1
#     elif(n2 > n1 & n2 > n3):
#         return n2
#     else:
#         return n3
# print("gratest number is:",num(4, 6, 7))

# ## 2nd que
# def tempConverter():
#     celcious = int(input("Enter celcious:"))
#     faranithe = ((celcious/5)*9) + 32
#     return faranithe
# print(tempConverter())

# ## 3rd que
# print("Hello", end = " ")
# print("How", end = " ")
# print("Are", end = " ")
# print("You?", end = " ")

# ## 4th que
# def reqursive(n):
#     sum = (n*(n+1))/2
#     return sum
# print(reqursive(100))

## 5th que
def decending():
    n = int(input("Enter a num:"))
    for i in range(n):
        print("*" * (n-i))
decending()
