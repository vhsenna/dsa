from typing import List


def search(nums: List[int], target: int) -> int:
    p1, p2 = 0, len(nums) - 1

    while p1 <= p2:
        middle = (p1 + p2) // 2

        if target < nums[middle]:
            p2 = middle - 1
        elif target > nums[middle]:
            p1 = middle + 1
        else:
            return middle
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
