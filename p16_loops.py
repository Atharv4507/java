i = 0
while i < 10:
    print("Yes " + str(i))
    i = i + 1
print("Done\n")

j = 0
while j <= 50:
    print(j)
    j = j + 1
print(" ")

f = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
print(f)
k = 0
while k < len(f):
    print(f[k])
    k = k + 1
print(" ")

for i in range(1, 8):
    print(i)
    # i = i + 1  -> not required
print(" ")

for i in range(1, 8, 2):
    print(i)
print(" ")

for i in range(10):
    print(i)
else:
    print("This is inside else of for")
print(" ")


for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")  # it will not print
print(" ")

for i in range(10):
    if i == 5:  # it will not print "5"
        continue
    print(i)
else:
    print("This is inside else of for")
print(" ")

n = 4
if n > 0:
    pass
while n > 6:
    pass
print("atharv is a good boy")
