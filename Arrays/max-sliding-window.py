
from collections import deque


def max_sliding_window(nums, k):
    max_deque = deque()
    l = r = 0
    output = []
    while r < len(nums):
        # keep queue monotonically increasing
        while max_deque and nums[max_deque[-1]] <= nums[r]:
            max_deque.pop()
        max_deque.append(r)
        if l > max_deque[0]:
            max_deque.popleft()
        if (r+1) >= k:
            output.append(nums[max_deque[0]])
            # make sure window is proper size before incrementing l
            l += 1
        r += 1

    return output


# output: [3, 3, 5, 5, 6, 7]
print(max_sliding_window([-1, -3, -3, -3, 3, 3], k))