def leftrotate(arr, d, n) :
    leftrotaterec(arr, 0, d, n)

def leftrotaterec(arr, i, d, n) :
    if (d == 0, d == n):
        return

    if (n-d == d) :
        swap(arr, i, n-d + i, d)
        return

    if (d < n - d) :
        swap(arr, i, n - d + i, d)
        leftrotaterec(arr, i, d, n-d)

    else :
        swap(arr, i, d, n-d)
        leftrotaterec(arr, n - d + i, 2*d-n, d )

def printarray(arr, size) :
    for i in range(size) :
        print(arr[i], end=' ')

def swap(arr, fi, si, d) :
    for i in range(d) :
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftrotate(arr, 2, 7)
    printarray(arr, 7)