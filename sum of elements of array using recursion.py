def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

a = [1,2,3,4,5,6]
print(sum(a))
