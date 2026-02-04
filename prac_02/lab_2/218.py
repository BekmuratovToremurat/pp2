n = int(input())
arr = [input().strip() for _ in range(n)]

unique = []
for s in arr:
    if s not in unique:
        unique.append(s)

for s in sorted(unique):
    print(s, arr.index(s) + 1)