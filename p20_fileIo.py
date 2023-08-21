f = open('sample.txt', 'r') #by default mode is r  #for write its 'w'
data = f.read()    #you can read the contain only onne time
# data = f.read(6)
print(data)
f.close()


d = open('sample1.txt','w')
d.write("Please write this to the file")
f.close()

with open('sample.txt','r') as f:
    a = f.read()
with open('sample.txt', 'w') as f:
    a = f.write("me")
print(a)