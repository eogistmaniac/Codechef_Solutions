for _ in range(int(input())):
    (h,c,t) = map(float,input().split())
    status = 0
    if h > 50:
        status = status + 1
    if c < 0.7:
        status = status + 2
    if t > 5600:
        status = status + 4
    if status == 7:
        print(10)
    elif status == 3:
        print(9)
    elif status == 6:
        print(8)
    elif status == 5:
        print(7)
    elif status == 0:
        print(5)
    else:
        print(6)
