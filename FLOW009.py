n =int(input())
c =0
for i in range(n):
    l = list(map(int,input().split()))
    if(l[0] > 1000):
        c = l[0]*l[1]
        c = c-(c*0.1)
        print("{:.6f}".format(c))
    else:
        print("{:.6f}".format(l[0]*l[1]))
