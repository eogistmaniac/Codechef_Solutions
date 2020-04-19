n = int(input())
b=[]
a=0
for i in range(0,n):
    l = list(map(int,input().split()))
    a = l[0]%l[1]
    b.append(a)
a=0
for i in range(0,len(b)):
    print(b[i])
            
