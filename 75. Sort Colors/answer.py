class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        color_count = [0,0,0]
        for color in nums:
            color_count[color] += 1

        Red,White,Blue = color_count
        nums[:Red] = [0] * Red
        nums[Red:Red+White] = [1] * White
        nums[Red+White:] = [2] * Blue
        
        # N = len(nums)
        # i=0
        # j=0
        # while i < N-1:
        #     j += 1
        #     if nums[i] > nums[j]:
        #         nums[i], nums[j] = nums[j], nums[i]
        #     if j == N-1:
        #         i += 1
        #         j = i