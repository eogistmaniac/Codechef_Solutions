n = int(input())
c=1
l=[]
for i in range(0,n):
    a = int(input())
    while(a>0):
        c=c*a
        a=a-1
    l.append(c)
    c=1
for i in range(0,len(l)):
    print(l[i])
