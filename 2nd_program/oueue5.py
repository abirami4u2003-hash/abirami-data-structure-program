class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x
        print(x, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Deleted:", self.queue[self.front])
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        print("Queue:", self.queue)


q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()
q.display()

q.enqueue(40)
q.enqueue(50)

q.display()