def findClosestNumber(self, nums: List[int]) -> int:
    ans = float("inf")

    for num in nums:
        if abs(num) < abs(ans):
            ans = num
        elif abs(num) == abs(ans):
            ans = max(num, ans)

    return ans