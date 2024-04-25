from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hasher = {}

    for idx, num in enumerate(nums):
        if hasher.get(num) is not None:
            return [hasher.get(num), idx]
        hasher[target - num] = idx


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
