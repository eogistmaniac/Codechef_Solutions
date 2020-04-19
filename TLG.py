n =int(input())
a = 0
b = 0
l = []
g = []
for i in range (0,n):
    x,y = input().split()
    a = a+int(x)
    b = b+int(y)
    if(a>b):
        d = a-b
        l.append(d)
    else:
        d = b - a
        g.append(d)
if(max(l)>max(g)):
    print("1",max(l))
else:
    print("2",max(g))
