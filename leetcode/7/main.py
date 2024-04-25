def reverse(x: int) -> int:
    reverse = int(str(abs(x))[::-1])

    if abs(reverse) >= 2 ** 31:
        return 0

    if x < 0:
        return -reverse
    return reverse


print(reverse(123))
print(reverse(-123))
print(reverse(120))
