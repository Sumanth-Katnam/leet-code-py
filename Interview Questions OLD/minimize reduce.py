import heapq
def minimizeCost(arr):
    heapq.heapify(arr)
    sum = 0
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        sum += first + second
        heapq.heappush(arr, first + second)
    return sum


def minimizeCostB(arr):
    arr.sort()
    first = arr[0]
    sum = 0
    for i in range(1, len(arr)):
        sum += first + arr[i]
        first = sum
    return sum


print(minimizeCost([30, 10, 20]))
print(minimizeCost([100, 1]))
print(minimizeCostB([30, 10, 20]))
print(minimizeCostB([100, 1]))