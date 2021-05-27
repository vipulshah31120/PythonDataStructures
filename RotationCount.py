def countrotate(arr, low, high) :
    if(high < low) :                                # this condition is needed when the array is not rotated at all
        return 0
    if (high == low) :                              # if there is only one element left
        return low

    mid = low + (high - low) / 2                    # Finding Mid
    mid = int(mid)

    if(mid < high and arr[mid] > arr[mid + 1]) :    # To check if element (mid+1) is minimum element
        return (mid + 1)

    if (mid > low and arr[mid] < arr[mid - 1]) :    # To check if mid itself is the minimum element
        return mid

    if(arr[high] > arr[mid]) :                      # Decide whether we need to go to left half or right half
        return countrotate(arr, low, mid - 1)
    return countrotate(arr, mid + 1, high)

arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countrotate(arr, 0, n - 1))



