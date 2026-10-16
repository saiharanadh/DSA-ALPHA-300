def Numbersdisappeared(nums):
    n = len(nums)
    present = [False] * (n + 1)

    for num in nums:
        if 1 <= num <= n:
            present[num] = True

    result = []

    for i in range(1, n + 1):
        if not present[i]:
            result.append(i)

    return result

print(Numbersdisappeared([1, 2, 4, 6, 8, 9]))