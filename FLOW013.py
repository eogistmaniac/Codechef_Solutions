n = int(input())
for i in range(0,n):
    a,b,c = map(float,input().split())
    z = a+b+c
    if(z == 180):
        print("YES")
    else:
        print("NO")
