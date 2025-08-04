def maxProfit(self, prices: List[int]) -> int:
    cur = float('inf') 
    profit = 0
    for price in prices:
        if price < cur:
            cur = price
        profit = max(profit, (price - cur))

    return profit
    