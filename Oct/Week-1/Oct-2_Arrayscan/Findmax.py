def Findmax(arr):
    maximum = arr[0]#initialize maximum with the first element

    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]#update maximum if a larger element is found

    return maximum

print(Findmax([3, 9, 2, 15, 6]))