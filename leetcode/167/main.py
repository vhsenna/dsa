def twoSum(numbers: list[int], target: int) -> list[int]:
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        sum = numbers[p1] + numbers[p2]

        if sum > target:
            p2 -= 1
        elif sum < target:
            p1 += 1
        else:
            return [p1 + 1, p2 + 1]

    return []


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))
