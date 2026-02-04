#Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})