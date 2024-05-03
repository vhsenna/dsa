from typing import List


def validMountainArray(arr: List[int]) -> bool:
    p1 = 0
    p2 = -1

    while p1 < (len(arr) - 1) and arr[p1] < arr[p1 + 1]:
        p1 += 1
    while p2 > -len(arr) and arr[p2] < arr[p2 - 1]:
        p2 -= 1

    return p1 == p2 + len(arr) and p1 > 0 and p2 < -1


print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
print(validMountainArray([1, 3, 2]))
