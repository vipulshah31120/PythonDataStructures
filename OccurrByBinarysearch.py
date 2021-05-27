def binarysearch(arr, l, r, x) :                    # l and r are index values
    if(r < l) :
        return -1

    mid = int(l + (r-1) / 2)                        # finding the middle index

    if arr[mid] == x :                              # If element is present in the middle itself
        return mid

    if arr[mid] > x :                               # if element is smaller than mid then it will only be present at left
        return binarysearch(arr, l, mid-1, x)

    else :                                          # If arr[mid] < x , we find x after mid which is (mid+1)
        return binarysearch(arr, mid + 1, r, x)

def countoccurrences(arr, n, x) :                   # Returns number of times x occurs in arr[0..n-1]
    ind = binarysearch(arr, 0, n - 1, x)            # Count = last index - 1st index + 1
    if ind == -1 :
        return 0

    count = 1                                       # Count elements on the left side
    left = ind - 1
    while (left >= 0 and arr[left] == x) :
        count += 1
        left -= 1

    right = ind + 1                                 # Counts elements on the right side
    while(right < n and arr[right] == x) :
        count += 1
        right += 1

    return count

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]                # It will only give occurrence of consecutive numbers
n = len(arr)
x = 2
print(countoccurrences(arr, n, x))
