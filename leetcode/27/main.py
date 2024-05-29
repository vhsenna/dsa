def removeElement(nums: list[int], val: int) -> int:
    p1 = 0

    for p2 in range(len(nums)):
        if nums[p2] != val:
            nums[p1] = nums[p2]
            p1 += 1
    return p1


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
