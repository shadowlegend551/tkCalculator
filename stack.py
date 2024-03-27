class Stack:
    # Different stack instances share the same start_value list
    # in memory if directly set!???!??!?!?!?!?
    # Have to create a new list instance for each stack instance.
    def __init__(self, start_value=None):  # start_value=[] causes a problem.
        self.stack = [] if start_value == None else start_value


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

