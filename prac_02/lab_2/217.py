n = int(input())
counts = {}

for _ in range(n):
    number = input().strip()
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

result = 0
for number in counts:
    if counts[number] == 3:
        result += 1

print(result)