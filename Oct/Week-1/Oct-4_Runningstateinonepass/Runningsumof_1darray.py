def RunningSum(arr):
    sum = 0
    result = []

    for num in arr:
        sum = sum + num
        result.append(sum)

    return result
print(RunningSum([1, 2, 3, 4]))