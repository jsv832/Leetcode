def removeDuplicates(self, nums: List[int]) -> int:

    N = len(nums)
    i = 0
    j = 1

    while j < N:
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j+=1 

    return i+1
