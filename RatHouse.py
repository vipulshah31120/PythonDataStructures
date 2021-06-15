r = int(input())
unit = int(input())
arr = list(map(int, input().split(None)))

def NoOfHouses() :
    t = r*unit
    sum = 0
    ans = 0
    for i in range (0, len(arr)) :
        if sum >= t :
            break
        else :
            sum += arr[i]
        ans += 1
    return ans
print('r: ', r)
print('unit: ', unit)
print('No.of Houses Sufficient for rats: ',NoOfHouses())


