import heapq

# trick: keeping the heap at size k

class KthLargest:
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


def kth_largest(nums, k):
    k_largest = heapq.nlargest(k, nums)
    return k_largest[k-1]

arr_1 = [3,2,1,5,6,4]
k_1 = 2
print(kth_largest(arr_1, k_1))

arr_2 = [3,2,3,1,2,4,5,5,6]
k_2 = 4
print(kth_largest(arr_2, k_2))