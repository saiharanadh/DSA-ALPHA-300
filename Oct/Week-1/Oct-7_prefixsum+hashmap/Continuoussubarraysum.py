def ContinuousSubarraySum(arr, k):
    remainder = {0: -1}
    prefix = 0

    for i in range(len(arr)):
        prefix = prefix + arr[i]
        rem = prefix % k

        if rem in remainder:
            if i - remainder[rem] >= 2:
                return True
        else:
            remainder[rem] = i
    return False
print(ContinuousSubarraySum([23, 2, 4, 6, 7], 6))