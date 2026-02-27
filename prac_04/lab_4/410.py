def cycle_list(lst, n):
    for _ in range(n):
        for item in lst:
            yield item
lst = input().split()
n = int(input())
first = True
for elem in cycle_list(lst, n):
    if not first:
        print(" ", end="")
    print(elem, end="")
    first = False