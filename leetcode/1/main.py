def twoSum(nums: list[int], target: int) -> list[int]:
    hasher = {}

    for index in range(len(nums)):
        complement = target - nums[index]
        if complement in hasher:
            return [hasher[complement], index]
        hasher[nums[index]] = index


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
