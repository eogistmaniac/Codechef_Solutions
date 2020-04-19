n = int(input())
for i in range(n):
    x =int(input())
    if(x<1500):
        hra = x*0.1
        da = x*0.9
        print(x+hra+da)
    else:
        hra = 500
        da = x*0.98
        print(x+hra+da)
