n = int(input())
c = 0
e =[]
for i in range(0,n):
    a = int(input())
    while(a>0):
        b = a%10
        c = (c*10)+b
        a = a//10
    e.append(c)
    c=0
for i in range(0,len(e)):
    print(e[i])
    

