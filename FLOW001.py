n = int(input())
l = []
for i in range(0,n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    z = x+y
    l.append(z)
for i in range(0,len(l)):
    print(l[i])    
