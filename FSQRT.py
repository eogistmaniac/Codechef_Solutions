import math
n = int(input())
c =[]
for i in range(0,n):
    a = int(input())
    b = int(math.sqrt(a))
    c.append(b)
for i in range(0,len(c)):
    print(c[i])
