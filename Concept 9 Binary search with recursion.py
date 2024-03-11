def binary_search_recursive(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)

        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, high, target)

    else:
        # Element is not present in the array
        return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10

# Function call
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

