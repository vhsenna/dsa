from typing import List


def maxProfit(prices: List[int]) -> int:
    if len(prices) == 0:
        return 0

    max_profit = 0
    min_value = prices[0]

    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - min_value)
        min_value = min(min_value, prices[i])
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
