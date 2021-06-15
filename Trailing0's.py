n = int(input())
print('Number of trailing Zeroes in :', n,'!')

def Trailing(n) :
    count = 0
    while(n>=5) :
        n = n//5
        count+=n
    return count
print(Trailing(n))

