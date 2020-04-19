n = int(input())
for i in range(0,n):
    x = int(input())
    a = x//100
    b = x%100
    c = b//50
    d = b%50
    e = d//10
    f = d%10
    g = f//5
    h = f%5
    i = h//2
    j = h%2
    print(int(a+c+e+g+i+j))
    
