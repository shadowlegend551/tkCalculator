class Queue:
    def __init__(self):
        self.queue = []


    def push(self, value) -> None:
        self.queue.append(value)


    def pop(self):
        return self.queue.pop(0) if len(queue) else None


    def check(self):
        return self.queue[0] if len(queue) else None
