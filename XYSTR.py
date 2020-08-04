for _ in range(int(input())):
    a = input()
    z = list(a)
    c = 0
    i = 0
    while(i<(len(z)-1)):
        if(z[i] != z[i+1]):
            i = i + 2
            c = c + 1
    print(c)