def printArray(A, size) :
    for i in range (size) :
        print(A[i], end=' ')
    print()

def SelectionSort(A, n) :
    for i in range (len(A)-1) :
        index = i
        for j in range (len(A)-1) :
            if A[index] > A[j] :
                index =  j
        print('while i = ', str(i))
        print('Minimum Element= ', str(A[index]))
        A[i] , A[index] = A[index] , A[i]
        print('Elements Swapped: ',str(A[i]), '&', str(A[index]))
    print('Array after ', str(len(A)) , 'iterations')
    printArray(A, n)
    print()

if __name__ == '__main__':
    A = [15, 11, 14, 12, 18]
    print('Unsorted Array')
    printArray(A, len(A))
    print()

    SelectionSort(A, len(A))

    print('Sorted Array')
    printArray(A, len(A))

