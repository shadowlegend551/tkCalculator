class Stack:
    def __init__(self, start_value=[]):
        self.stack = start_value


    def push(self, value) -> None:
        self.stack.append(value)


    def pop(self):
        return self.stack.pop(-1) if len(self.stack) else None


    def check(self):
        return self.stack[-1] if len(self.stack) else None


    def length(self) -> int:
        return len(self.stack)


    def isEmpty(self) -> bool:
        return False if len(self.stack) else True
