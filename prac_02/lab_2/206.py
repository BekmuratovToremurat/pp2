a=int(input())
arr=list(map(int, input().split()))
max=arr[0]
for i in arr:
    if i>max:
        max=i
print(max)