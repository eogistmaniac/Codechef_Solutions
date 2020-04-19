n =int(input())
c = 0
for i in range(n):
    x = int(input())
    d = x
    while(x>0):
        a = x%10
        c = (c*10)+a
        x = x//10
    if(c == d):
        print("wins")
    else:
        print("losses")
    c=0
    
