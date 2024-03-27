class Stack:
    def __init__(self):
        self.stack = []


    def push(self, value) -> None:
        self.stack.append(value)


    def pop(self):
        return self.stack.pop(-1) if len(stack) else None


    def check(self):
        return self.stack[-1] if len(stack) else None
