def isPalindrome(x: int) -> bool:
    reverse = 0
    xCopy = x

    while x > 0:
        d = x % 10
        reverse = reverse * 10 + d
        x = x // 10

    if abs(x) >= 2 ** 31:
        return False

    if xCopy == reverse:
        return True
    else:
        return False


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
