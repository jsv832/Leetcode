def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda interval: interval[0])
    ans = [intervals[0]]
    intervals.sort()
    for interval in intervals:
        if interval[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], interval[1])
        else:
            ans.append(interval)
    return ans