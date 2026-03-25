import re
a=input()
x=re.findall("^Hello.*world$", a)
if x:
    print("good")
else:
    print("not")