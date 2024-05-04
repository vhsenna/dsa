def lengthOfLastWord(s: str) -> int:
    words = s.split()

    if words:
        return len(words[-1])
    else:
        return 0


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
