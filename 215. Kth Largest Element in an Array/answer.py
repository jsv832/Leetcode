def findKthLargest(self, nums: List[int], k: int) -> int:
    for i in range(len(nums)):
        nums[i] *= -1

    heapq.heapify(nums)

    while k > 1:
        heapq.heappop(nums)
        k -= 1


    return -(nums[0])