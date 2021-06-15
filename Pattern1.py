n = int(input())
k = n
m = n*2

for i in range(1, m+1) :
    if i<n :
        print('* '*k)
        k-=1
    else :
        print('* '*k)
        k+=1
print('--------------------------------------------------------------------------------------------')

n = int(input())
k = n
m = n*2

for i in range(1, m) :
    if i<n :
        print(' '*(n - k), end='*'*k)
        print()
        k-=1
    else :
        print(' '*(n - k), end='*'*k)
        print()
        k+=1