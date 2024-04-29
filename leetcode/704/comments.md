# Binary Search

Given an array of integers, `num`, in ascending order, and an integer called `target`, write a function to find the `target` in the array and return its index. If not found, return -1.

The algorithm should be written with O(log n) runtime complexity.

---

We start with two pointers `p1` and `p2` pointing respectively to the first and last index. We also start with a pointer at the middle index of the array, called `m`.

Next, we compare the value of pointer `m` with the `target`.

If `target` is less than `m`, we move `p2` to a position before `m` and move `m` to the midpoint between `p1` and `p2`.

Otherwise, if `target` is greater than `m`, we move `p1` to a position after `m` and move `m` to the midpoint between `p1` and `p2`.

If `m` is equal to `target`, we have found the answer. If `p1` and `p2` converge to the same index, then the `target` does not exist in the array.
