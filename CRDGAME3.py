import math
for _ in range(int(input())):
    chef,rick = map(int,input().split())
    q1 = math.ceil(chef/9)
    q2 = math.ceil(rick/9)
    if(q1 == q2):
        print(1,q2)
    if(q1 < q2):
        print(0,q1)
    if(q1 > q2):
        print(1,q2)