n = input()
a = float(n.split(" ")[0])
b = float(n.split(" ")[1])       
if((a+0.5)<b and (a%5)==0):
    c = b-(a+0.5)
    print("{:.2f}".format(c))
else:
    print("{:.2f}".format(b))    
