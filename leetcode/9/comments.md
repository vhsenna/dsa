# Palindrome Number

Given an integer, determine if it's a palindrome without converting it to a string.

---

To achieve this, we'll create a reversed version of the original number (`int`) and compare it with the original. If they match, the number is a palindrome.

First, we'll initialize a variable (`reverse`) to store the reversed number.

We'll also create a copy of `x` for later comparison.

Since the problem requires a solution without string conversion, we'll utilize a while loop with the following approach:

- Extract the last digit of `x` using the modulo operator. For example, `x % 10 = d`.
- Add this last digit (`d`) to `reverse` using the formula `10 * reverse + d`.
- Discard the last digit of `x` using `x / 10`.

Repeat these steps for the remaining digits. After each iteration, `x` will shrink by one digit. Terminate the loop when `x = 0`, indicating no digits remain to be reversed.

Finally, compare `reverse` with the copy of `x`, as the original value was modified during the iteration.
