from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    unique = set()

    for num in nums:
        if num in unique:
            return True
        unique.add(num)
    return False


print(containsDuplicate([1, 2, 1, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
