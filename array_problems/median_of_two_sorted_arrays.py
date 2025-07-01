def medianOfTwoSortedArrays(arr1, arr2):
    arr = arr1 + arr2
    sorted_arr = sorted(arr)
    count = len(sorted_arr)
    middle = count // 2


    if count % 2 == 0:
        return (sorted_arr[middle-1] + sorted_arr[middle]) / 2
    else:
        return sorted_arr[middle]


arr1 = [1,2]
arr2 = [3,4]
result = medianOfTwoSortedArrays(arr1, arr2)
print(result)
