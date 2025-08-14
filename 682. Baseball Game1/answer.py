def calPoints(self, operations: List[str]) -> int:
    ans = 0
    stack = []
    for op in operations:
        if op == 'D': 
            stack.append(int(stack[-1]) * 2)
        elif op == 'C':
            stack.pop()
        elif op == '+':
            stack.append(int(stack[-1]) + int(stack[-2]))
        else:
            stack.append(op)
    
    for num in stack:
        ans += int(num)
    return ans