def findMaxAverage(self, nums: List[int], k: int) -> float:
    ans = float("-inf") 
    cur = 0
    for i in range(k):
        cur += nums[i]
    ans = cur

    for i in range(k, len(nums)):
        cur += nums[i]
        cur -= nums[i-k]
        ans = max(ans, cur)

    return ans/k
