import re

s = input()
pattern = input()

pattern = re.escape(pattern)

matches = re.findall(pattern, s)

print(len(matches))