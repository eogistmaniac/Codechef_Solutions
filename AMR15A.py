n = int(input())
l = list(map(int,input().split()))
c = 0
d = 0
for i in range(0,len(l)):
    if(l[i]%2 == 0):
        c = c+1
    else:
        d = d+1
if(c > d):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
    
