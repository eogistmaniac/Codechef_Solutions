n = int(input())
l=[]
c=0
for i in range(0,n):
    a = int(input())
    while(a>0):
        b = a%10
        c = c+b
        a = a//10
    l.append(c)
    c=0
for i in range(0,len(l)):
    print(l[i])
