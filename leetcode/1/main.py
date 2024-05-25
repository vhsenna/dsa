def twoSum(nums: list[int], target: int) -> list[int]:
    hasher = {}

    for index, num in enumerate(nums):
        if hasher.get(num) is not None:
            return [hasher.get(num), index]
        hasher[target - num] = index


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
