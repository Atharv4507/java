# ## 1st que
# n = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")
# print(" ")

# ## 2nd que
# l1 = ["harry", "sohan","sachine","rahul"]
# for name in l1:
#     if name.startswith("s"):
#         print("hello " + name)
# print(" ")

# ## 3rd que
# n = int(input("Enter a number:"))
# prime = True
# for i in range(2,n):
#     if(n%i == 0):
#         prime = False
#         break
# if prime:
#     print("This num is prime")
# else:
#     print("This num is not prime")
# print(" ")

# ## 4th que
# n = int(input("Enter a number:"))
# i = 1
# while i < 11:
#     print(n*i)
#     i = i+1
# print(" ")

# ## 5th que
# n = int(input("Enter a number:"))
# print(f"sum of number {n} is: {(n*(n+1))/2}")
# print(" ")

# ## 6th que
# n = int(input("Enter a number:"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"The factorial of {n} is {fact}")
# print(" ")

# ## 7th que
# n = int(input("Enter a number:"))
# for i in range(n):
#     print("*" * (i+1))
# print(" ")

# ## 8th que
# n = int(input("Enter a number:"))
# for i in range(n):
#     print(" " * (n-i-1), end = "")
#     print("*" * (2*i+1), end = "")
#     print(" " * (n-i-1))
# print(" ")

## 9th que
n = int(input("Enter a number: "))
for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print("*",end=" ") 
    print(" ") #or down one
for i in range(n):
    print("*"*(n-i))
print(" ")
