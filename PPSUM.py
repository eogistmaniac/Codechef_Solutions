def sum(d,n):
    sum = 0
    for i in range(d):
        for j in range(1,(n+1)):
            sum=sum+j
        n = sum
        j = sum
        sum =0
    print(j)
n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    sum(l[0],l[1])
