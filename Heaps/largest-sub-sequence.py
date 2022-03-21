# You are given an integer array nums and an integer k.
#   You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
#   A subsequence is an array that can be derived from another array by deleting some
#   or no elements without changing the order of the remaining elements.

# Constraints:
#
# 1 <= nums.length <= 1000
# -105 <= nums[i] <= 105
# 1 <= k <= nums.length

# Need to maintain order of subsequence; subsequence does NOT have to sequential i.e for
#   [-1,-2,3,4], 3 should result in [-1, 3, 4]; indexes need to be maintained

"""
Potential improvement: store the value and it's index together
"""

import heapq
import math

def max_subsequence(nums, k):
    nums_copy = nums.copy()
    n_largest = heapq.nlargest(k, nums_copy)
    indices = []
    for element in n_largest:
        indices.append(nums_copy.index(element))
        nums_copy[nums_copy.index(element)] = -math.inf

    output = []
    indices.sort()
    for index in indices:
        output.append(nums[index])

    return output

test_nums = [18,3,19,-8,30,22,-35,11,16,18,-21,32,-7,-6,38,25,-21,-1,26,-8,-37,-39,-34,6,-36,-3,26,-32,22,-20,35,-35,-30,-8,11,7,-23,-9,-22,1,33,-6,12,2,27,-27,28,-12,21,12,16,21,33]
k = 50
print(max_subsequence(test_nums, k))

