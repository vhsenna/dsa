def isPalindrome(s: str) -> bool:
    s = s.lower()

    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        if not s[p1].isalnum():
            p1 += 1
        elif not s[p2].isalnum():
            p2 -= 1
        elif s[p1] != s[p2]:
            return False
        else:
            p1 += 1
            p2 -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
