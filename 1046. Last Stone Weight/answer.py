def lastStoneWeight(self, stones: List[int]) -> int:
    for i in range(len(stones)):
        stones[i] *= -1

    heapq.heapify(stones)
    while len(stones) > 1:
        a = heapq.heappop(stones)
        b = heapq.heappop(stones)
        
        if a != b:
            heapq.heappush(stones, (a-b))
    if stones:
        return -stones[0]
    else:
        return 0

