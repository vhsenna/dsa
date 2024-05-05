from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if not nums:
        return 0

    for index, num in enumerate(nums):
        if num >= target:
            return index

    return len(nums)


print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
