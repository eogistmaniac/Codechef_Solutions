import math
g =[]
n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    a = math.gcd(l[0],l[1])
    lcm = (l[0]*l[1])//a
    g.append(a)
    g.append(lcm)
    print(*g)
    g=[]
