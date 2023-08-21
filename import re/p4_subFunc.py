import re
str = "How are you, How is everithing"
matches = re.sub("How", "where", str)
print(matches)
