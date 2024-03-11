def linearSearch(array, target):
    n = len(array)
    for i in range(n):
        if array[i] == target:
            return i
    return -1


arr = [2, 45, -34, 18, 87, 90, 67, 3, 78, 13]
target = 45

print(linearSearch(arr, target))
