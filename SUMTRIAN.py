n =int(input())
for i in range(n):
    x = int(input())
    l=[]
    for i in range(x):
        a = list(map(int, input().split()))
        l.append(a)
    for i in range(x-1,0,-1):
        for j in range(i):
            arr[i-1][j] += max(arr[i][j],arr[i][j+1])
print(arr[0][0])
