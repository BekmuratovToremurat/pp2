def powers_of_two(n):
    value = 1
    for _ in range(n + 1):
        yield value
        value *= 2
n = int(input())
first = True
for num in powers_of_two(n):
    if not first:
        print(" ", end="")
    print(num, end="")
    first = False