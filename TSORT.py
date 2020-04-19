n=int(input())
l=[]
for i in range(0,n):
    a = int(input())
    l.append(a)
l.sort()
for i in range(0,len(l)):
    print(l[i])
