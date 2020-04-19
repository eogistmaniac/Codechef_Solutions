n =int(input())
no_of_trgls = 0
for i in range(n):
    size = int(input())
    no_of_times = size//2
    size=size-2
    for i in range(0,no_of_times):
        no_of_trgls = no_of_trgls + size//2
        size = size-2
    print(no_of_trgls)
    no_of_trgls = 0
