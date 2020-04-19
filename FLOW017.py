n = int(input())
a = []
for i in range(n):
    l = list(map(int,input().split()))
    l.sort()
    a.append(l[1])
for i in range(0,len(a)):
    print(a[i])
