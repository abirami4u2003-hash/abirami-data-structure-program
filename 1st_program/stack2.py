class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Stack is empty"

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.stack)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Stack:", s.stack)