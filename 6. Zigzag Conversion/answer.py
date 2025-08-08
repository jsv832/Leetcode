def convert(self, s: str, numRows: int) -> str:

    if numRows == 1:
        return s
        
    n = numRows
    S = len(s)
    temp = [[] for _ in range(n)]
    ans = ''
    i=0

    while i < S:
        for vert in range(n):
            if i < S:
                temp[vert].append(s[i])
                i += 1

        for diag in range(n-2,0,-1):
            if i < S:
                temp[diag].append(s[i])
                i += 1

    for line in temp:
        ans += ''.join(line)

    return ans