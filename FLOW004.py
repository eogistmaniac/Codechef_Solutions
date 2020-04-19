n=int(input())
c=0
d=[]
for i in range(0,n):
    b = input()
    l=list(b)
    e = len(l)
    c=int(l[0])+int((l[e-1]))
    d.append(c)
l=[]
for i in range(0,len(d)):
    print(d[i])
