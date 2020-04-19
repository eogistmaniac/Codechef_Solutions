n = int(input())
for i in range(n):
    x = list(input())
    if(len(x)%2 == 0):
        a = x[:len(x)//2]
        b = x[len(x)//2:]
        a.sort()
        b.sort()
    else:
        c = ((len(x)+1)//2)-1
        x.remove(x[c])
        a = x[:len(x)//2]
        b = x[len(x)//2:]
        a.sort()
        b.sort()
    if(a == b):
        print("YES")
    else:
        print("NO")

