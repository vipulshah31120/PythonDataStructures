def recursion_fact(n) :
    if (n == 1) :                   # Base case for recursion.
        return n
    else :
        return n * recursion_fact(n-1)   # Call recursively with lesser number.
        #print(result)

n = int(input())
if n <0 :
    print('Negative value not accepted')
elif n==0 :
    print('Factorial of 0 is 1')
else :
    print(recursion_fact(n))


