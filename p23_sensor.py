with open("sample2.txt") as f:
    content = f.read()
content = content.replace("fucking", "*******")
with open("sample2.txt",'w') as f:
    f.write(content)