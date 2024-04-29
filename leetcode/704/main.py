from typing import List


def search(nums: List[int], target: int) -> int:
    p1, p2 = 0, len(nums) - 1

    while p1 <= p2:
        m = (p1 + p2) // 2

        if target < nums[m]:
            p2 = m - 1
        elif target > nums[m]:
            p1 = m + 1
        else:
            return m
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
