# Find Numbers with Even Number of Digits

Given an array `nums`, return the count of numbers in the array that have an even number of digits.

For example, consider `nums = [12, 345, 2, 6, 7896]`:

12 has two digits

345 has 3 digits

2 has 1 digit

6 has 1 digit

7896 has 4 digits

So, only 12 and 7896 have an even number of digits.

---

Considering the problem constraints, we observe that the range of numbers in the list is `1 <= num <= 100000`.

To have an even number of digits, a number must fall within the range `[10, 99]` or `[1000, 9999]`, or it must be `100000`.
