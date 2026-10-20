def SubarraySum(arr, k):
    count = {0: 1}
    prefix = 0
    result = 0

    for num in arr:
        prefix = prefix + num

        if prefix - k in count:
            result = result + count[prefix - k]

        if prefix in count:
            count[prefix] = count[prefix] + 1
        else:
            count[prefix] = 1

    return result

print(SubarraySum([1, 1, 1], 2))