import math
n = int(input())
a =0
for i in range(n):
    x = int(input())
    a,b = map(int,input().split())
    f,g = map(int,input().split())
    h,i = map(int,input().split())
    f = ((f-a)**2)+((g-b)**2)
    k = ((h-f)**2)+((i-g)**2)
    d = math.sqrt(f)
    o = math.sqrt(k)
    a = d+o
    if(a<=x):
        print("yes")
    else:
        print("no")
