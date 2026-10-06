class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(value, "inserted")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            value = self.stack[self.top]
            self.top -= 1
            print("Deleted:", value)

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Top:", self.stack[self.top])

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack:", end=" ")
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()


s = Stack(5)

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()
s.pop()
s.display()
