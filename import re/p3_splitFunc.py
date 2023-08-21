import re
print("1")
str = "How are you, How is everithing"
matches = re.split(",", str)
print(matches)
matches = re.split("is", str)# no differance
print(matches,"\n")
str = "\aHow are you, How is everithing"
matches = re.split(",", str)
print(matches,"\n")
str = "\A How are you, How is everithing"
matches = re.split(",", str)
print(matches,"\n")
str = "\b How are you, How is everithing"
matches = re.split(",", str)
print(matches,"\n")
str = "\B How are you, How is everithing"
matches = re.split(",", str)
print(matches,"\n")
str = "\d How are you, How is everithing"
matches = re.split(",", str)
print(matches)
# print(matches.reverse())
# print(matches.append("How"))
# print(matches.insert(13, "How"))
