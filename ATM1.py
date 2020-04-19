x,y=input().split()
x=float(x)
y=float(y)
if x%5==0 and x+0.50<y:
    y=y-(x+0.50)
    print(round(y,2))
else:
    print(round(y,2))
