# 3Sum

This problem asks to find all sets of three numbers in a list of integers where the sum of these three numbers equals zero. However, the solution set cannot contain duplicate triplets, and none of the indices of the elements in the triplet can be the same.

For example, considering the input list nums = [-1, 0, 1, 2, -1, -4], the expected result is a list of lists containing all sets of three numbers that sum up to zero.

In this case, a possible solution would be [-1, -1, 2] and [-1, 0, 1], because (-1) + (-1) + 2 = 0 and -1 + 0 + 1 = 0.

The order in which the triplets are presented does not matter, but each triplet within the solution set must be unique. For example, [0, -1, 1] and [-1, 1, 0] are considered duplicates, and only one of them should be included in the output list.

---

The problem presents us with an unsorted array. Our first step is to sort this array in ascending order, which simplifies subsequent operations. Without sorting, we'd need to resort to a hashmap, making the solution significantly more complex.

In the Two Sum II problem (167), we utilized two pointers—one starting from the array's first element and the other from the last. They traversed towards the middle of the array until identifying the value that summed up to the target.

In this problem, involving three elements instead of two, we adapt the Two Sum II strategy. We iterate through the array, fixing one element (e.g., the first element) and employing the two-pointer approach for the remaining elements.

Consider the example of the given list nums = [-1, 0, 1, 2, -1, -4]. Sorting it yields nums = [-4, -1, -1, 0, 1, 2].

We start the loop with the first number in the sorted list, -4.

Setting the first pointer to the subsequent element (-1) and the second pointer to the last element of the list (2), we check if their sum equals zero.

If the sum is less than 0, we advance the first pointer to the next index, in this case, the element with a value of -1.

If the sum exceeds zero, we move the second pointer to the previous index in the list.

In the scenario mentioned, we exhaust all permutations involving the first element of the sorted list, -4, but find no solution. Consequently, we can discard the element -4 from further consideration.

Following that, the while loop progresses to the second element of the sorted array, namely, -1, and continues accordingly.

Upon identifying a sum of 0, the three discovered elements are appended to a list of lists.
