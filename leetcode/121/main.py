def maxProfit(prices: list[int]) -> int:
    p1, p2 = 0, 1
    max_profit = 0

    while p2 < len(prices):
        if prices[p1] < prices[p2]:
            profit = prices[p2] - prices[p1]
            max_profit = max(max_profit, profit)
        else:
            p1 = p2
        p2 += 1

    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
