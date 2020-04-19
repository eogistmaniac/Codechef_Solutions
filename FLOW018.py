import math
n = int(input())
l=[]
for i in range(0,n):
    a = int(input())
    b = math.factorial(a)
    l.append(b)
for i in range(0,len(l)):
    print(l[i])
