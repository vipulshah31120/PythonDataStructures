#1
n = int(input())
for i in range(1, n+1) :
    print('*  '*i)

print('--------------------------------------------------------------------------------------------')

#2
n = int(input())
for i in range(n, 0, -1) :
    print('*  '*i)

print('--------------------------------------------------------------------------------------------')

#3
n = int(input())
for i in range(1, n+1) :
    print(' '*(n-i), end='*'*i)
    print()

print('---------------------------------------------------------------------------------------------')
                                #3 & #4 are same-- difference is an extra space at end=' *'
#4
n = int(input())
for i in range(1, n+1) :
    print(' '*(n-i), end=' *'*i)
    print()

print('----------------------------------------------------------------------------------------------')

#5
n = int(input())
for i in range(n, 0, -1) :
    print(''*(n-1), end='*'*i)
    print()

print('----------------------------------------------------------------------------------------------')
#6
n = 5
for i in range(1, n+1) :
    print('* '*n)
print('---------------------------------------------------------------------------------------------- ')

#7
n = int(input())
for i in range(1, n+1) :
    if i == (n//2+1) :
        print('*'*n)
    else :
        print(''*(n//2),' * ')

