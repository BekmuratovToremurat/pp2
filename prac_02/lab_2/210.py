n=int(input())
arr=list(map(int, input().split()))
newarr=sorted(arr)
newarr.reverse()
for i in newarr:
    print(i, end=" ")