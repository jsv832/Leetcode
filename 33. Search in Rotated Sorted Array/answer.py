def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l+r) //2
        if nums[r] < nums[m]:
            l = m+1
        else:
            r = m
            l = 0
    low_i = l

    if low_i == 0:
        l= 0
        r= r = len(nums) - 1
    elif target >= nums[0] and target <= nums[low_i-1]:
        l = 0
        r = low_i - 1
    else:
        l= low_i
        r = len(nums) - 1
    
    while l <= r:
        m = (l+r) //2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m+1
        else:
            r = m-1
    return -1
