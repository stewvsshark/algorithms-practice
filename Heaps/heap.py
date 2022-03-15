
# A basic min & max heap implementation
class Heap:
    def __init__(self, input_arr=None):
        if input_arr is None:
            self.heap = []
            self.size = 0
        else:
            self.heap = input_arr
            self.size = len(self.heap)

    def _swap_nodes(self, node1, node2):
        tmp = self.heap[node1]
        self.heap[node1] = self.heap[node2]
        self.heap[node2] = tmp

    def peak(self):
        if self.size < 1:
            return None

        return self.heap[0]


class MinHeap(Heap):
    def __init__(self, input_arr=None):
        super().__init__(input_arr)
        self._build_min_heap()

    def _min_heapify(self, k):
        l = (2*k)+1
        r = (2*k)+2

        if l < self.size and self.heap[l] < self.heap[k]:
            smallest = l
        else:
            smallest = k

        if r < self.size and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != k:
            tmp = self.heap[k]
            self.heap[k] = self.heap[smallest]
            self.heap[smallest] = tmp
            self._min_heapify(smallest)

    def _build_min_heap(self):
        start_node = (len(self.heap)-1)//2
        while start_node >= 0:
            self._min_heapify(start_node)
            start_node -= 1

    def heappop(self):
        if self.size > 0:
            root = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap = self.heap[:-1]
            self.size -= 1
            self._min_heapify(0)
            return root
        else:
            return None

    def _siftup(self, k):
        if k <= 0:
            return
        parent = (k-1)//2
        if self.heap[k] < self.heap[parent]:
            self._swap_nodes(k, parent)
            self._siftup(parent)

    def heappush(self, element):
        self.heap.append(element)
        self.size += 1
        self._siftup(self.size - 1)


# ----------------- Max Heap --------------- #
class MaxHeap(Heap):
    def __init__(self, input_arr=None):
        super().__init__(input_arr)
        self._build_max_heap()

    def _max_heapify(self, k):
        l = (2*k)+1
        r = (2*k)+2

        if l < self.size and self.heap[l] > self.heap[k]:
            largest = l
        else:
            largest = k

        if r < self.size and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != k:
            tmp = self.heap[k]
            self.heap[k] = self.heap[largest]
            self.heap[largest] = tmp
            self._max_heapify(largest)

    def _build_max_heap(self):
        start_node = (len(self.heap)-1)//2
        while start_node >= 0:
            self._max_heapify(start_node)
            start_node -= 1

    def heappop(self):
        if self.size > 0:
            root = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap = self.heap[:-1]
            self.size -= 1
            self._max_heapify(0)
            return root
        else:
            return None

    def _siftup(self, k):
        if k <= 0:
            return
        parent = (k-1)//2
        if self.heap[k] > self.heap[parent]:
            self._swap_nodes(k, parent)
            self._siftup(parent)

    def heappush(self, element):
        self.heap.append(element)
        self.size += 1
        self._siftup(self.size - 1)


# creates min heap from seed - output [-5, 15, 0, 100, 25, 10, 1]
test_min_heap_seeded = MinHeap([10, 25, -5, 100, 15, 0, 1])
print(test_min_heap_seeded.heap)

test_min_heap = MinHeap()       # create an empty heap
test_min_heap.heappop()         # noop (error check)
test_min_heap.peak()            # noop (error check)
test_min_heap.heappush(1)       # heap: [1]
test_min_heap.heappop()         # heap: []
test_min_heap.heappop()         # noop: error check
test_min_heap.heappush(-1)      # heap: [-1]
test_min_heap.heappush(-100)    # heap: [-100, -1]
test_min_heap.heappush(100)     # heap: [-100, -1, 100]
print(test_min_heap.heap)

test_max_heap = MaxHeap()       # create empty max heap
test_max_heap.heappop()         # noop (error check)
test_max_heap.peak()            # noop (error check)
test_max_heap.heappush(1)       # heap: [1]
test_max_heap.heappop()         # heap: []
test_max_heap.heappush(-1)      # heap: [-1]
test_max_heap.heappush(-100)    # heap: [-1, -100]
test_max_heap.heappush(100)     # heap: [100, -100, -1]
print(test_max_heap.heap)
