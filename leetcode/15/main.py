from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    solution = []

    for index, num in enumerate(nums):
        if index > 0 and num == nums[index - 1]:
            continue

        p1, p2 = index + 1, len(nums) - 1

        while p1 < p2:
            threeSum = num + nums[p1] + nums[p2]
            if threeSum > 0:
                p2 -= 1
            elif threeSum < 0:
                p1 += 1
            else:
                solution.append([num, nums[p1], nums[p2]])
                p1 += 1
                while nums[p1] == nums[p1 - 1] and p1 < p2:
                    p1 += 1

    return solution


print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 1, 1]))
print(threeSum([0, 0, 0]))
