def printarray (A, size) :
    for i in range(size) :
        print(A[i], end=' ')
    print()

def insertionsort(array, size) :
    for i in range(1, size) :
        key = array[i]
        j = i-1
        print('while i = ', str(i))
        print('Element = ',str(array[i]))
        while j>=0 and key<array[j] :
            array[j+1] = array[j]
            print('Element shifted is: ', str(array[j]))
            j-=1
        array[j+1] = key
        print('Array after', {str(i)}, 'iterations: ',(i+1))
        printarray(array, size)                     #During Sorting
        print('\n')

if __name__ == '__main__':
    A = [15, 11, 12, 14, 18]
    print('Unsorted Array')
    printarray(A, len(A))
    print()

    insertionsort(A, len(A))

    print('Sorted Array: ')
    printarray(A, len(A))

