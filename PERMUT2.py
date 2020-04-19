x = int(input())
a = []
while(x!=0):
    l = list(map(int,input().split()))
    for j in range(1,x+1):
        a.append((l.index(j)+1))
    if(a == l):
        print("ambiguous")
    else:
        print("not ambiguous")
    a =[]
    x = int(input())
