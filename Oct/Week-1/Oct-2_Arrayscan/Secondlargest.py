def Secondlargest(arr):
    largest = None
    second_largest = None

    for i in range(len(arr)):
        if largest is None or arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]

    if second_largest is None:
        return -1

    return second_largest

print(Secondlargest([12, 35, 1, 10, 34, 1]))