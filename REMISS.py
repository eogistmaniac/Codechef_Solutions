n = int(input())
for i in range(0,n):
    x,y = map(int,input().split())
    if(x>=y):
        print(x,x+y)
    else:
        print(y,x+y)
