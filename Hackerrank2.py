N, M  = map(int,input().split())
s1 = '.|.'
s2 = 'WELCOME'

# upper part
for i in range(N//2) :
    print((s1 * ((i * 2) + 1)).center(M, '-'))

#centre part
print(s2.center(M, '-'))

#lower part
for i in range(N//2 - 1, -1, -1) :
    print((s1 * ((i * 2) + 1)).center(M, '-'))

