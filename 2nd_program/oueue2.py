class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

    def display(self):
        print("Queue:", self.queue)

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
print("Deleted:", q.dequeue())
q.display()