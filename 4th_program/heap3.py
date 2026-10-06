import heapq

def kth_largest(arr, k):
    heap = []

    for value in arr:
        heapq.heappush(heap, value)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


arr = [10, 5, 20, 8, 15, 30]
k = 3

print("Array:", arr)
print(k, "rd largest element:", kth_largest(arr, k))
