def is_valid_number(n):
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            return False
        n //= 10
        
    return True
number = int(input())
if is_valid_number(number):
    print("Valid")
else:
    print("Not valid")