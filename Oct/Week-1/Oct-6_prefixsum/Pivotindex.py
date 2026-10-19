def Pivotindex(nums):
    total = 0

    for num in nums:
        total = total + num

    leftsum = 0

    for i in range(len(nums)):
        rightsum = total - leftsum - nums[i]

        if leftsum == rightsum:
            return i

        leftsum = leftsum + nums[i]

    return -1

print(Pivotindex([1, 7, 3, 6, 5, 6]))