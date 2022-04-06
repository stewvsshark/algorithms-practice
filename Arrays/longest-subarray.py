from collections import deque

# Given an array of integers nums and an integer limit, return the size of the longest non-
#   empty subarray such that the absolute difference between any two elements of this subarray
#   is less than or equal to limit.

# Notes:
# this class of problem is probably pretty common - find the longest/shortest subarray that obeys some
#   property
# the property in this case is basically the absolute difference between the min element and the max element
#   of the current subarray is <= limit
# when needing to fetch forward elements from current index, may be easier to use while loop
# sliding window in a loop is a useful construct
# Use two queues:
#   What we can do is to have two pointers: left and right,
#   and then find the longest subarray for every right pointer (iterate it) by shrinking left
#   pointer. And return the longest one among them.
#   The two queues help us keep track of the min and max values of a respective subarray:
#       one queue holds the indices of min values, increasing monotonically
#       one queue holds the indices of the max values, decreasing monotonically
# In the beginning, we set both left pointer l and right pointer r at index 0. We keep moving r forward until
#   the max absolute difference within the window exceeds the limit. Then, we move forward l
#   until the max absolute difference falls back within the limit.
#   Operations:
#       - Pop (from end) all indices from the min queue that point to larger values than the current r pointer (queue clean up)
#       - Pop (from end) all indices from the max queue that point to smaller values than the current r pointer (queue clean up)
#       - While the current max - current min > limit:
#           - increment left pointer
#           - if l pointer value > current min, pop current min
#           - if l pointer value > current max, pop current max
# Related problem (probably a good starter problem):
#   Find the maximum of a given sliding window in an array
#   Find the minimum of a given sliding window in an array

def longest_subarray(nums, limit):
    max_subarray_length = 1
    for i, element in enumerate(nums):
        sub_heap = [element]
        scanning = True
        j = i + 1
        while scanning:
            if j == len(nums):
                return max(max_subarray_length, len(sub_heap))

            sub_heap.append(nums[j])
            if abs(min(sub_heap) - max(sub_heap)) <= limit:
                j = j+1
            else:
                if len(sub_heap) - 1 > max_subarray_length:
                    max_subarray_length = len(sub_heap) - 1
                scanning = False

def longest_subarray_alternate(nums, limit):
    min_deque, max_deque = deque(), deque()
    l = r = 0
    ans = 0
    while r < len(nums):
        while min_deque and nums[r] <= nums[min_deque[-1]]:
            min_deque.pop()
        while max_deque and nums[r] >= nums[max_deque[-1]]:
            max_deque.pop()
        min_deque.append(r)
        max_deque.append(r)

        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            l += 1
            if l > min_deque[0]:
                min_deque.popleft()
            if l > max_deque[0]:
                max_deque.popleft()

        ans = max(ans, r - l + 1)
        r += 1

    return ans



test_nums_1 = [8,2,4,7]
test_limit_1 = 4
print(longest_subarray_alternate(test_nums_1, test_limit_1))

test_nums_2 = [4,2,2,2,4,4,2,2]
test_limit_2 = 0
print(longest_subarray_alternate(test_nums_2, test_limit_2))


test_nums_3 = [10,1,2,4,7,2]
test_limit_3 = 5
print(longest_subarray_alternate(test_nums_3, test_limit_3))

test_nums_4 = [1,5,6,7,8,10,6,5,6]
test_limit_4 = 4
print(longest_subarray(test_nums_4, test_limit_4))
