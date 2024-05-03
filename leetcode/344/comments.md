# Reverse String

Write a function that reverses a string. The string is given as an array of characters.

The problem should be solved by modifying the input array in-place, using O(1) extra memory.

---

To solve this, start by placing a pointer `p1` at the first element of the array and another pointer `p2` at the last element of the array. Then, swap the values at the positions pointed by `p1` and `p2`.

Next, move `p1` one position forward and `p2` one position backward.

Continue this process until `p1` and `p2` meet, indicating that the entire array has been traversed.
