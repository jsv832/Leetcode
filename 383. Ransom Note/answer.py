def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    magazine_hash = Counter(magazine)

    for ch in ransomNote:
        if magazine_hash[ch] > 0:
            magazine_hash[ch] -= 1
        else:
            return False
    return True
