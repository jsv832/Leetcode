def productExceptSelf(self, nums: List[int]) -> List[int]:
    ans = [1] * len(nums)
    left = 1
    for l in range(0, len(nums)):
        ans[l] *= left
        left *= nums[l]

    right = 1 
    for r in range(len(nums)-1,-1, -1):
        ans[r] *= right
        right *= nums[r]

    return ans