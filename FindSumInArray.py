def findpivot(arr, n, x) :                      # This function returns count of number of pairs with sum equals to x.
    for i in range(n) :                         # Pivot element is largest element in the array
        if arr[i] > arr[i+1] :
            break

    l = (i + 1) % n                             # l is the index of smallest element
    r = i                                       # r is the index of the largest element
    cnt = 0                                     # variable to store count of number of pairs

    while(l != r):                              # Find sum of pair formed by arr[l] and arr[r] and update l, r, cnt accordingly
        if arr[l] + arr[r] == x :               # if sum=x , increment cnt and move l and r to net element
            cnt += 1
            if l == (r - 1 + n) % n :           # this condition is required so that l and r shouldn't cross each other
                return cnt
            l = (l + 1) % n
            r = (r - 1 + n) % n

        elif arr[l] + arr[r] < x :              # if current sum is greater move to lower sum side
            l = (l + 1) % n

        else :
            r = (n + r - 1) % n
    return cnt


arr = [11, 15, 6, 7, 9, 10]
s = 16
print(f'Total times the sum {s} is present:  ')
print(findpivot(arr, 6, s))


