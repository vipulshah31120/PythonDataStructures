#d = elements
# Function to left rotate arr[] of size n by d

def leftrotate(arr, d, n) :
    g_c_d = gcd(d, n)
    for i in range (g_c_d) :
        temp = arr[i]                # move i-th values of blocks
        j = i
        while 1 :
            k = j+d
            if k>= n :               # The element have to be rotated
                k = k-n
            if k == i :              # The element is already in rotated position
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def printarray(arr, size) :
    for i in range (size) :
        print(arr[i], end=' ')

def gcd(a, b) :                     # Function to get gcd of a and b
    if b==0 :
        return a
    else :
        return gcd(b,a % b )        #gcd(d,n) blocks are made

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftrotate(arr, d, n)
printarray(arr, n)

