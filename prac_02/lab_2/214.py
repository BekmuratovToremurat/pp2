n = int(input())
arr = list(map(int, input().split()))

max_count = 0
answer = arr[0]

for i in range(n):
    count = 0
    for j in range(n):
        if arr[j] == arr[i]:
            count += 1

    if count > max_count:
        max_count = count
        answer = arr[i]
    elif count == max_count:
        if arr[i] < answer:
            answer = arr[i]

print(answer)
