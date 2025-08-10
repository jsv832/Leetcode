def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for x in range(len(nums)):
        diff = target - nums[x]
        if diff in seen:
            return ([seen[diff],x ])
        seen[nums[x]] = x
    return []
