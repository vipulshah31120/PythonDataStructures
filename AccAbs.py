n = int(input())
arr = list(map(int, input().split(None, n)[:n]))

def AccAbs(arr) :
    ans = 0
    arr.sort()
    for i in range(1, len(arr)) :
        ans += (arr[i] - arr[i - 1])
    return ans
print(AccAbs(arr))

