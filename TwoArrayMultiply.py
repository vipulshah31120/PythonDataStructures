def TwoArray(arr1, arr2) :
    arr2.reverse()
    if len(arr1) == 0 or len(arr2) == 0 :
        return -1
    else :
        l = len(arr1)
        su = 0
        for i in range(l) :
            su += arr1[i] * arr2[i]
            #print(arr1, arr2, su)
        return su
arr1 = [28, -8, 8, 6, -34]
arr2 = [23, 18, 20, -8, -3]
    #print(arr1, arr2, su)
print(TwoArray(arr1, arr2))