def isSubsequence(self, s: str, t: str) -> bool:
    S = len(s)
    T = len(t)
    if S == 0:
        return True

    if S > T:
        return False

    count = 0
    for i in range(T):
        if t[i] == s[count]:
            if count == S-1:
                return True
            count += 1
    return False
