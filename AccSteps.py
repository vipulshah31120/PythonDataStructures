# To find the minimum steps to reach the given number
n = int(input())
c = 0
while n>0 :
    if n % 2 == 0:              # For Even
        n = n//2
    else :                      # For Odd
        n = n-1
    c+=1
print(c)
