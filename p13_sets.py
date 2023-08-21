a = {1,3,4,5} # its set
print((type(a)))
print(a)

# but,{} -> its not empty set its "dict()"
#ex.
b = {}
print(type(b))

#creating empty set
b = set()
print(type(b))


# Methods
#1 adding value
b.add(4)
b.add(5)
b.add(2)
b.add(12)
# we cant add list in it  and also dict too
# Ex: b.add([2,3,4])   -> Error

#but we can add tuple in it 
# Ex: b.add((2,3,4))
b.add((2, 3, 4))

print(b)

#2 length
print(len(b))

#3 remove
b.remove(5)
print(b)

#4 pop 
# removes random num in the set 
b.pop()
print(b)

#5 clear
b.clear()
print(b)

#6 union
c = {1,2,3,4,5,6,7,8,9}
d = {7,8,9,10,11,12,13}

print(c.union({11,12,13,1,3}))
print(c.union(d))

#7 intersection
print(c.intersection(d))