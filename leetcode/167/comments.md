# Two Sum II - Input Array Is Sorted

The problem provides an indexed array of integers, `numbers`, which is already sorted in non-decreasing order. The task is to find two numbers within this array that add up to a specific number, `target`.

Ultimately, the solution should return the indices of these two numbers in an array.

---

Given the example of an array `numbers = [2, 7, 11, 15]` and `target = 9`, the most straightforward way to solve this problem is to sum all possible combinations within the array until finding the result.

For example, summing 2+7, 2+11, 2+15, 7+11, 7+15, 11+15, etc.

This solution would work at some point. Luckily, the result would be found on the first attempt (2 + 7), but this solution has a time complexity of O(n²).

However, if the array is very long, this solution won't be performant.

Each item in the array exponentially increases the time to find the result.

A simple and performant solution is to use two pointers, traversing the array only once. The notation for this solution is O(n), meaning it depends solely on the size of the array.

The solution is to use two pointers. Since the array is in ascending order, we can initialize the first pointer (`p1`) at the first element of the array, and the second pointer (`p2`) at the last element of the array.

Next, we compare whether the sum of the two pointers is greater or less than the target.

If it's less, we move the first pointer (`p1`) to the next element of the array. Since the array is in ascending order, moving the first pointer (`p1`) to the next element means that now the sum of the two elements will either remain the same or increase.

If the sum of the two pointers is greater than `target`, then we move the second pointer (`p2`) to the previous index.

This way, the array will be traversed from start to end and end to start simultaneously, and the result will be found by traversing only once, hence the Big O notation will be in the order of O(n).
