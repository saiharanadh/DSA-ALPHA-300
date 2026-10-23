def LongestSubarraySum(arr, k):
    prefix = 0
    longest = 0
    first_index = {0: -1}

    for i in range(len(arr)):
        prefix = prefix + arr[i]

        if prefix - k in first_index:
            length = i - first_index[prefix - k]

            if length > longest:
                longest = length

        if prefix not in first_index:
            first_index[prefix] = i

    return longest

print(LongestSubarraySum([10, 5, 2, 7, 1, 9], 15))