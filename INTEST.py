x,y = input().split()
x=int(x)
y=int(y)
a=[]
k=0
for i in range(0,x):
    b=int(input())
    a.append(b)
for j in range(0,x):
    if(a[j]%y==0):
        k = k+1
    else:
        pass
print(k)
    
