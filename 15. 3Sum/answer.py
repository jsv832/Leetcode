def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n - 2):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            summ = nums[i] + nums[l] + nums[r]
            if summ == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif summ > 0:
                r -= 1
            else:
                l += 1
    return ans
