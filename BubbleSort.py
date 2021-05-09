def printArray(A, size) :
    for i in range (size) :
        print(A[i], end=' ')
    print()

def bubblesort(arr, n) :
    for i in range (n-1) :
        for j in range(0, n-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print('In-Pass', str(i+1))
                print(str(arr[j+1]), '&' , str(arr[j]), 'are swapped')
                printArray(arr, n,)
        print('Array after Pass: ', i+1)
        printArray(arr, n)
    print()

if __name__ == '__main__':
    A=[15, 11, 14, 12, 18]
    print('Unsorted Array')
    printArray(A, len(A))
    print()

    bubblesort(A, len(A))

    print('Sorted Array')
    printArray(A, len(A))
