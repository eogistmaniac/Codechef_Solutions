n = int(input())
b=[]
for i in range(0,n):
    a = int(input())
    b.append(a)
d = min(b)
for i in range(0,len(b)):
    if(b[i]!=d):
        b[i] = b[i]-d
for i in range(0,len(b)):
    print(b[i])
    
