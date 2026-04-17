class MinStack:
    
    def __init__(self):
        self.stack= []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        smallestnum= 0
        for i in range (len(self.stack)):
            if i== 0:
                smallestnum= self.stack[i]
            elif self.stack[i]<smallestnum:
                smallestnum= self.stack[i]
        return smallestnum
