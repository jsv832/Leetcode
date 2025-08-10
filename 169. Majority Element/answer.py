def majorityElement(self, nums: List[int]) -> int:
    ans = 0
    count = 0

    for num in nums:
        if count == 0:
            ans = num

        count += 1 if num == ans else -1

    return ans
