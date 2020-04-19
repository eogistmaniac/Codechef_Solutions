t=int(input())
while(t):
    t-=1 
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    print(s[1]+s[0])
