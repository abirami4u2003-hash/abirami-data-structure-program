import heapq

priority_queue = []

# Insert items
heapq.heappush(priority_queue, (2, "Complete assignment"))
heapq.heappush(priority_queue, (1, "Attend class"))
heapq.heappush(priority_queue, (3, "Play games"))
heapq.heappush(priority_queue, (1, "Submit record"))

print("Priority Queue:")

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print("Priority:", priority, "Task:", task)
