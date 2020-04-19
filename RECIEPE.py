import math
n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    h=[]
    a,b,c = l[0],l[1],l[1:]
    for j in range(a):
        b = math.gcd(b,c[j])
    for z in c:
        q = z//b
        h.append(q)
    print(*h)
        
             
