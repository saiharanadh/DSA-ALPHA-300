def Reversearray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]#swap the two elements
        left += 1
        right -= 1

    return arr

print(Reversearray([1, 2, 3, 4, 5]))