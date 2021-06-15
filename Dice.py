n = int(input())
c = 0

if n>0 and n<=12:
    for i in range(1, 7) :
        for j in range(1, 7) :
            if i+j == n :
                c+=1
    print(c)
else :
    print(0)
