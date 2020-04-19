n = int(input())
k = 0
j = 1
for i in range(0,n):
    x = int(input())
    a = x
    while(j<=x):
        c = a%j
        if(c == 0):
            k =k + 1
        a = x
        j = j+1
    j=1
    if(k > 2):
        print("no")
    if(k == 2):
        print("yes")
    k=0
