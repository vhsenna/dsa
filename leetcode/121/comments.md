# Best Time to Buy And Sell Stock

You're given an array called `prices`, where `prices[i]` represents the price of a particular stock on the i-th day.

Your objective is to maximize your profit by selecting a day to buy the stock and choosing a different day in the future to sell it.

Return the maximum profit you can make from this transaction. If you cannot make any profit, return `0`.

---

Problems of this nature are commonly referred to as sliding window.

We begin with three variables, `p1`, `p2`, and `max_profit`. `p1` and `p2` are pointers that initially point to the first and second positions in the array, respectively. `max_profit` is initialized to zero.

If `p2` is less than `p1`, both pointers are advanced to the next positions.

If `p2` is greater than `p1`, we compare the difference between `p2` and `p1` with the current `max_profit`.If the difference is greater, we update `max_profit`. Otherwise, we continue advancing `p2`.

However, there is an even better solution. In fact, we can eliminate the need for `p1` since we don't require the position of the value in the list. Instead, we can use a variable to store the smallest value encountered so far (`min_value`). This simplifies the algorithm, as we now only need to iterate through the list once with a single for loop.
