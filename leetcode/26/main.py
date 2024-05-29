def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    p2 = 1

    for p1 in range(1, len(nums)):
        if nums[p1] != nums[p1 - 1]:
            nums[p2] = nums[p1]
            p2 += 1

    return p2


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
