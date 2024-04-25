# Longest Consecutive Sequence

Given a list of integers, the goal is to return the size of the largest possible set of consecutive numbers.

For example, in the list [100, 4, 200, 1, 3, 2], the expected return value is 9.

Similarly, in the list [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], the expected return value is 4.

The solution must be implemented with a time complexity of O(n).

---

To solve this problem, the first step is to sort the array in ascending order.

Once sorted, we only need to keep track of the count of consecutive numbers and the size of the largest sequence found in memory.

It's important to note in the algorithm that duplicate numbers should be skipped.

To accomplish this, we'll introduce a variable to represent the previous number in the array, initially set to 0.5 to ensure it doesn't coincide with any integer values in the array.
