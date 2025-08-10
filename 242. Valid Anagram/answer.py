def isAnagram(self, s: str, t: str) -> bool:

    s_hash = Counter(s)
    t_hash = Counter(t)

    if s_hash == t_hash:
        return True
    else:
        return False