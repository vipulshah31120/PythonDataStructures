def reversearray(arr, start, end ) :
    while(start < end) :                        # start is the index element
        temp = arr[start]
        arr[start] = arr[end]                   # elements at start will be assigned by elements at end
        arr[end] = temp                         # element stored at temp will be assigned in the end
        start += 1                              # increment start
        end -=1                                 # decrement end

def leftrotate(arr, d) :
    if d == 0 :
        return
    n = len(arr)

    d = d % n                                   # in case the rotating factor is greater than array length

    reversearray(arr, 0, d-1)                   # Abr= reverse from index(start) to element d [(d-1) is the index]
    reversearray(arr, d, n-1)                   # Bbr = reverse from dth element to nth element [(n-1) is the index]
    reversearray(arr, 0, n-1)                   # (AbrBbr)r = reverse from starting(index) to end

def printarray(arr) :
    for i in range(0, len(arr)) :
        print(arr[i], end=' ')


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftrotate(arr, d)                             # Rotate array by 2
printarray(arr)