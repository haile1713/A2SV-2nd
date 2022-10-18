class MyQueue:

    def __init__(self):
        self.t1 =[]
        self.t2 =[]
        

    def push(self, y: int) -> None:
        while self.t1:
            self.t2.append (self.t1.pop())
        self.t1.append (y)
        while self.t2:
             self.t1.append (self.t2.pop())
    def pop(self) -> int:
        return self.t1.pop()
    def peek(self) -> int:
        return self.t1[-1]

    def empty(self) -> bool:
        return not self.t1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
