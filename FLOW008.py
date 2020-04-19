n = int(input())
l=[]
for i in range(0,n):
    a =int(input())
    l.append(a)
for i in range(0,len(l)):
    if(l[i]<10):
        print("What an obedient servant you are!")
    else:
        print(-1)
