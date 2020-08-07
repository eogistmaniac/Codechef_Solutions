for _ in range(int(input())):
    n , k = map(int,input().split())
    pos = list(map(int,input().split()))
    moves = []
    final =[]
    j = 0
    for i in range(0,len(pos)):
        if(k%pos[i] == 0):
            temp = k//pos[i]
            moves.append(temp)
            final.append(pos[i])
            j = 1
    if( j == 1):
        index = moves.index(min(moves))
        print(final[index])
    else:
        print(-1)



