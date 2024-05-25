def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]

    return nums


print(runningSum([1, 2, 3, 4]))
print(runningSum([1, 1, 1, 1, 1]))
print(runningSum([3, 1, 2, 10, 1]))
