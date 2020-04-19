n = int(input())
for i in range(n):
    x = int(input())
    l = input()
    a = list(l)
    count1 = a.count("I")
    count2 = a.count("Y")
    if(count1>0 and count2 == 0):
        print("INDIAN")
    if(count2>0 and count1 ==0):
        print("NOT INDIAN")
    if(count2 == 0 and count1 == 0):
        print("NOT SURE")
    
