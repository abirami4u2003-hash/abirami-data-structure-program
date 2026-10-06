queue = []

def enqueue(x):
    queue.append(x)
    print(x, "inserted")

def dequeue():
    if queue:
        print("Deleted:", queue.pop(0))
    else:
        print("Queue is empty")

def display():
    print("Queue:", queue)

enqueue(10)
enqueue(20)
enqueue(30)

display()
dequeue()
display()