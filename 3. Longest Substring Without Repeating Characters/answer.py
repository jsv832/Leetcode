def lengthOfLongestSubstring(self, s: str) -> int:
    l= 0
    sub = set()
    ans = 0
    for r in range(len(s)):
        while s[r] in sub:
            sub.remove(s[l])
            l += 1
        sub.add(s[r])
        cur = r-l + 1
        ans = max(ans, cur)

    return ans