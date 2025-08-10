def maxNumberOfBalloons(self, text: str) -> int:
    t_hash = Counter(text)

    return min(t_hash['b'], t_hash['a'], t_hash['l'] // 2, t_hash['o'] // 2, t_hash['n'])