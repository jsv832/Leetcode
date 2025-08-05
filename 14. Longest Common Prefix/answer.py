def longestCommonPrefix(self, strs: List[str]) -> str:
    max_length = float("inf")
    strs.sort()

    for string in strs:
        max_length = min(max_length, len(string))

    i = 0
    while i < max_length:
        for string in strs[0:]:
            if strs[0][i] != string[i]:
                return strs[0][:i]x
        i += 1

    return strs[0][:i]