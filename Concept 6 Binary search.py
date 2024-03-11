def binarySearch(array, target):
    l = 0
    u = len(array) - 1
    while l <= u:
        mid = (l + u) // 2
        if array[mid] == target:
            return mid
        else:
            if array[mid] <= target:
                l = mid + 1
            else:
                u = mid - 1
    return -1

arr = [1,45,78,89,99,101,123]
target = 123
print(binarySearch(arr, target))
