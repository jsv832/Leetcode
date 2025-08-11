def sortedSquares(self, nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1
    ans = []

    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            ans.append(nums[l] **2)
            l +=1
        else:
            ans.append(nums[r] **2)
            r -=1

    ans.reverse()
    return ans

# def sortedSquares(self, nums: List[int]) -> List[int]:
# l = 0
# n = len(nums)
# r = n - 1
# ans = [0] * n
# i= 1

# while l <= r:
#     if abs(nums[l]) > abs(nums[r]):
#         ans[-i] = nums[l] **2
#         l +=1
#     else:
#         ans[-i] = nums[r] **2
#         r -=1
#     i +=1
    
# return ans