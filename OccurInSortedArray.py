def occurrence(arr, n, x) :
    res = 0
    for i in range(n) :                                 # Returns number of times x
        if x == arr[i] :                                # occurs in arr[0..n-1]
            res += 1
    return res

arr = [1, 2, 2, 2, 2, 3, 4, 2 ,8 ,8]
n = len(arr)
x = 2
print(occurrence(arr, n, x))
