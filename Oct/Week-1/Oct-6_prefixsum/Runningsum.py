def Runningsum(nums):
    prefix = []
    total = 0

    for num in nums:
        total = total + num
        prefix.append(total)

    return prefix

print(Runningsum([1, 2, 3, 4]))