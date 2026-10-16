def MissingNumber(arr):
    n = len(arr)

    totalsum = n * (n + 1) // 2
    actualsum = 0

    for num in arr:
        actualsum = actualsum + num

    return totalsum - actualsum

print(MissingNumber([0,1,3]))