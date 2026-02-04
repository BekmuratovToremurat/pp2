n = int(input())
result = set()

for _ in range(n):
    surname = input().strip()
    result.add(surname)

print(len(result))