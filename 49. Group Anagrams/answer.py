def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dic = defaultdict(list)

    for s in strs:
        word = "".join(sorted(s))
        dic[word].append(s)

    return list(dic.values())