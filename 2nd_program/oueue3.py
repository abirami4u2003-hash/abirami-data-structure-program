queue = []
size = 5

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if len(queue) < size:
            x = int(input("Enter value: "))
            queue.append(x)
            print("Inserted:", x)
        else:
            print("Queue Overflow")

    elif choice == 2:
        if queue:
            print("Deleted:", queue.pop(0))
        else:
            print("Queue Underflow")

    elif choice == 3:
        print("Queue:", queue)

    elif choice == 4:
        break

    else:
        print("Invalid choice")