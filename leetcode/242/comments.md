# Valid Anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

The first approach could be to sort both strings (`s` and `t`) and then compare their lengths. However, this is less efficient because sorting takes time proportional to O(n log n) where n is the length of the strings.

The second approach uses a hash table.

This approach counts how many times each character appears in string `s` and then subtracts the corresponding count for each character in string `t`. If `s` and `t` are anagrams, the counts for each character will cancel each other out, resulting in a dictionary with all zeros as values.

This method has a time complexity of O(n), where n is the total number of characters in both strings. It iterates over each character only once to count frequencies and then compares those frequencies, making it a more efficient solution for this problem.
