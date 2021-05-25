#Searches an element key in a pivoted sorted array arrp[] of size n
def pivotbinaryssearch(arr, n, key) :
    pivot = findpivot(arr, 0, n-1)

    if pivot == -1 :                                    #If we didn't find a pivot, then array is not rotated at all
        return binarysearch(arr, 0, n-1, key)

    if arr[pivot] == key :                              #If we found a pivot, then first compare with pivot and then
        return pivot
    if arr[0] <= key :                                  # search in two sub arrays around pivot
        return binarysearch(arr, 0, pivot-1, key)
    return binarysearch(arr, pivot+1, n-1, key)


def findpivot(arr, low, high) :                             #Function to get pivot. For array
    if high < low :
        return -1
    if high == low :
        return low

    # low + (high - low)/2;
    mid = int((low + high)/2)

    if mid < high and arr[mid] > arr[mid + 1] :
        return mid
    if mid > low and arr[mid] < arr[mid-1] :
        return (mid-1)
    if arr[low] >= arr[mid] :
        return findpivot(arr, low, mid-1)
    return findpivot(arr, mid+1, high)


#Standard Binary Search function
def binarysearch(arr, low, high, key) :
    if high<low :
        return -1

    mid = int((low+high)/2)
    if key == arr[mid] :
        return mid

    if key > arr[mid] :
        return binarysearch(arr, (mid+1), high, key)
    return binarysearch(arr, low, (mid-1), key)

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr)
key = 3
print('Index of element: ', pivotbinaryssearch(arr, n, key))
