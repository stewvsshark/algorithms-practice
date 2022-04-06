
from collections import deque


def min_sliding_window(nums, k):
    q = deque()
    l = r = 0
    output = []

    while r < len(nums):
        while q and nums[r] <= nums[q[-1]]:
            q.pop()
        q.append(r)
        if q[0] < l:
            q.popleft()
        if (r+1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output


# output: [-1, -3, -3, -3, 3, 3]
print(min_sliding_window([1,3,-1,-3,5,3,6,7], 3))