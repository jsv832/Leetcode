def summaryRanges(self, nums: List[int]) -> List[str]:
    ans = []
    N = len(nums)
    i = 0
    while i < N:
        start = nums[i]
        while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
            i += 1
        if nums[i] != start:
            ans.append(str(start) + '->' + str(nums[i]))
            i += 1
        else:
            ans.append(str(start))
            i += 1

    return ans