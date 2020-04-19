n = int(input())
for i in range(0,n):
    a,b = map(int,input().split())
    if(a>b):
        print(">")
    if(a<b):
        print("<")
    if(a==b):
        print("=")
        
