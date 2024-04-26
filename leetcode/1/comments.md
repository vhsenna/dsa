# Two Sum

The problem provides an array of integers and an integer called `target`. The goal is to return the indices of the two numbers in the array that, when added, result in the target.

Each number in the array must be used only once, and there should be only one solution.

---

There are three ways to solve this problem: the brute force, the good, and the best approach.

## 1st Solution: Brute Force
The first solution involves brute force and consists of creating loops to combine all elements until finding the answer. This solution has a time complexity of O(n²).

## 2nd Solution: Good Approach
The second solution involves sorting the array and using two pointers. First, we sort the array and then create two pointers, where the first pointer (`p1`) is set to the value of the element at index 0 of the sorted array, and the second pointer (`p2`) is set to the last element of the sorted array. After that, we check if the sum of the two pointers is greater than or equal to the target value. If the sum is less than the target, we move the first pointer (`p1`) to the next index. If the sum is greater, we move the second pointer (`p2`) to the previous index. This solution has a time complexity of O(n log n).

## 3rd Solution: Best Approach
The third and best solution involves using a hashmap. The algorithm traverses the array, and for each item in the array, calculates the value that, when added to the item, equals the target value. For example, given an array `[11, 15, 2, 7]` and a target of `9`, what value added to the first element of the array, 11, results in 9? The answer would be -2. Then, we store in the hashmap the value -2 and the position of the element 11, for example, `{-2: 0}`. With this hashmap, we can check for each item if it is already present in the hashmap. In the example, if the second element of the array were -2 and it was already in the hashmap, we would conclude that -2 is the complement of the element 11 to reach the target. In the end, the algorithm traverses the array only once.
