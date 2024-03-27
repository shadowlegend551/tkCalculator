class Queue:
    # Different queue instances share the same start_value list
    # in memory if directly set!???!??!?!?!?!?
    # Have to create a new list instance for each queue instance.
    def __init__(self, start_value=None):  # start_value=[] causes a problem.
        self.queue = [] if start_value == None else start_value


    def push(self, value) -> None:
        self.queue.append(value)


    def pop(self):
        return self.queue.pop(0) if len(self.queue) else None


    def check(self):
        return self.queue[0] if len(self.queue) else None


    def length(self) -> int:
        return len(self.queue)


    def isEmpty(self) -> bool:
        return False if len(self.queue) else True
