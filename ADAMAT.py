for _ in range(int(input())):
    n = int(input())
    operations = 0
    l1 =[]
    coloumn = n
    for  i in range(n):
        l = list(map(int,input().split()))
        l1.append(l)
    for i in range(n-1,0,-1):
        fixed_element = l1[i][i]
        changing_element = l1[i][i-1] + 1
        if(fixed_element != changing_element):
            operations = operations + 1
            c = i+1
            for i in range(c):
                for j in range(i,c):
                    l1[i][j],l1[j][i] = l1[j][i],l1[i][j]
    print(operations)