for _ in range(int(input())):
    health , power = map(int,input().split())
    g = 1
    while(power<health):
        if( power == 0 and health!=0):
            g = 0
            break
        health = health - power
        power = power / 2
    print(g)