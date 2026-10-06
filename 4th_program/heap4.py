import heapq

def kth_smallest(arr, k):
    heap = arr.copy()
    heapq.heapify(heap)

    for i in range(k - 1):
        heapq.heappop(heap)

    return heapq.heappop(heap)


arr = [25, 10, 5, 30, 15, 20]
k = 3

print("Array:", arr)
print(k, "rd smallest element:", kth_smallest(arr, k))
