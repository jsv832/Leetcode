def evalRPN(self, tokens: List[str]) -> int:
    stack = []

    for symbol in tokens:
        if symbol in "+-*/":
            b,a = stack.pop(), stack.pop()

            if symbol == '+':
                stack.append(a+b)
            elif symbol == '-':
                stack.append(a-b)
            elif symbol == '*':
                stack.append(a*b)
            else:
                stack.append(int(a/b))
        else:
            stack.append(int(symbol))
    return stack[-1]