def isValid(self, s: str) -> bool:
    stack = []
    for sign in s:
        if sign == '[':
            stack.append(']')
        elif sign == '(':
            stack.append(')')
        elif sign == '{':
            stack.append('}')
        else:
            if len(stack) > 0 and sign == stack.pop():
                continue
            else:
                return False