def longestConsecutive(self, nums: List[int]) -> int:
    ans = 1
    num_set = set(nums)
    if not nums:
        return 0
        
    for num in num_set:
        if (num - 1) not in num_set:
            cur_num = num
            cur_streak = 1
            while (cur_num + 1) in num_set:
                cur_num += 1
                cur_streak += 1
            ans = max(ans, cur_streak)
    return ans
