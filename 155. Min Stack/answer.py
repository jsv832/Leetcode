def __init__(self):
    self.Stack = []
    self.minStack= []

def push(self, val: int) -> None:
    self.Stack.append(val)
    if not self.minStack:
        self.minStack.append(val)
    elif self.minStack[-1] < val:
        self.minStack.append(self.minStack[-1])
    else:
        self.minStack.append(val)

def pop(self) -> None:
    self.Stack.pop()
    self.minStack.pop()
def top(self) -> int:
    return self.Stack[-1]

def getMin(self) -> int:
    return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()