t = int(input())
for i in range(t):
    price = int(input())
    menu = 0
    while(price!=0):
        k=1
        while(price>=k and k<=2048):
            k=k*2
            print(k)
        price = price - (k/2)
        print(price)
        menu = menu+1
        print("menu is:",menu)
    print(menu)
