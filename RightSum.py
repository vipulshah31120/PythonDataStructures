#Replace every element of array with sum of elements on its right side
#Input: arr[] = {1, 2, 5, 2, 2, 5}
#Output: 16 14 9 7 5 0

def replace(arr, n) :
    sum = 0

    for i in range(0, n) :
        sum += arr[i]

    for i in range(0, n) :
        arr[i] = sum - arr[i]
        sum = arr[i]

    for i in range (0, n) :
        print(arr[i], end=' ')

if __name__ == '__main__':
    arr = [1, 2, 5, 2, 2, 5 ]
    n = len(arr)
    replace(arr, n)