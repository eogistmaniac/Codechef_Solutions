n = int(input())
b=[]
for i in range(0,n):
    a = input()
    l = list(a)
    c = l.count("4")
    b.append(c)
l=[]
for i in range(0,len(b)):
    print(b[i])
