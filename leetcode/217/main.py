from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


print(containsDuplicate([1, 2, 1, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
