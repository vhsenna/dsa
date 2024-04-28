# Contains Duplicate

Given the array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

You can solve this problem using a set in Python to store the numbers you have encountered during the iteration through the array. If you find a number that is already in the set, it means that this number has appeared at least twice in the array.

The set named `unique` is used to store the numbers that have been seen. The loop iterates through the numbers in the array `nums`, and if a number is already in the set, the function returns `true`, indicating that we have found a duplicate number. If the loop finishes without finding any duplicate numbers, the function returns `false`.
