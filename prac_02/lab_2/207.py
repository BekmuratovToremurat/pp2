a=int(input())
arr=list(map(int, input().split()))
pos=1
max=arr[0]
for i in range(1,a):
    if arr[i]>max:
        max=arr[i]
        pos=i+1
print(pos)