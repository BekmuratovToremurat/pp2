n=int(input())
arr=list(map(int, input().split()))
max=arr[0]
min=arr[0]

for x in arr:
    if x>max:
        max=x
    if x<min:
        min=x

for i in range(n):
    if arr[i]==max:
        arr[i]=min

for x in arr:
    print(x, end=" ")