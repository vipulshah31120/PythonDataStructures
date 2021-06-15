def ispalindrome(s = input()) :
    return s == s[::-1]

ans = ispalindrome()

if ans :
    print('Yes')
else :
    print('No')

