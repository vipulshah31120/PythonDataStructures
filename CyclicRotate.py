def rotate(arr, n) :
    x = arr[n-1]                        # storing the last element in variable (x)
    for i in range(n-1, 0, -1) :        # iterating it backwards
        arr[i] = arr[i-1]               # update till the 1st position not 0th position
    arr[0] = x

arr = [1, 2, 3, 4, 5]
n = len(arr)

rotate(arr, n)
for i in range(0, n) :
    print(arr[i], end=' ')