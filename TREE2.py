for _ in range(int(input())):
    c = int(input())
    a = list(map(int,input().split()))
    b = set(a)
    if(0 in b):
        print(len(b)-1)
    else:
        print(len(b))