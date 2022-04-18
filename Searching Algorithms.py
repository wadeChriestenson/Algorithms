# Algorithms


# Searching Algorithms
# Linear Search
# Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of the elements, return -1.
# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1


def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
arr = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]
x = 10
n = len(arr)

# Function call
result = search(arr, n, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)


# Binary Search
# Search a sorted array by repeatedly dividing the search interval in half.
# Begin with an interval covering the whole array.
# If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise, narrow it to the upper half.
# Repeatedly check until the value is found or the interval is empty.

# Python3 Program for recursive binary search.

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Driver Code
arr = [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]
x = 9

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
