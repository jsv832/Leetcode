def maxProfit(self, prices: List[int]) -> int:
    ans = 0
    expensive = float("-inf")

    for price in reversed(prices):
        if price > expensive:
            expensive = price
        
        if price < expensive:
            ans += (expensive - price)
            expensive = price
    return ans
