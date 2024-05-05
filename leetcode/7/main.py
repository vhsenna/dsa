def reverse(x: int) -> int:
    reverse = int(str(abs(x))[::-1])

    if x < 0:
        return - reverse
    return reverse


print(reverse(123))
print(reverse(-123))
print(reverse(120))
