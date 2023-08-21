def percent(marks):
    p = ((marks[0] + marks[1] + marks[2])/300)*100
    return p
marks1 = [78, 89, 98]
percent1 = percent(marks1)

marks2 = [45, 45, 67]
percent2 = percent(marks2)

print(percent1, percent2)


def greet(name):
    print("Good day " + name)
greet("Atharv")
greet("Harry")


def sum(n1,n2):
    s = n1 + n2
    return s
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
print("Sum = ",sum(n1, n2))


