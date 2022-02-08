import heapq
import math

# You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)]
#   such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product
#   of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes
#   fewer than three elements).
# Note that the three largest elements used to form any product may have the same values as one another,
#   but they must be at different indices in arr.

# Questions
# 1. Can I use a library to do the heaping? - If someone has already solved this problem (assuming efficient solution)
#   no need to reinvent the wheel

# Crude solution: iterate every element and find 3 largest elements up to and including current element

# Optimal solution: use a heap to find largest elements in each a[0..i] subarray

def find_max_product(arr):
    arr_len = len(arr)
    result = [-1] * arr_len
    for i in range(2, arr_len):
        max_heap = heapq.nlargest(3, arr[0:i+1])
        result[i] = max_heap[0] * max_heap[1] * max_heap[2]

    return result



arr_1 = [1, 2, 3, 4, 5]
arr_2 = [2, 1, 2, 1, 2]

print(find_max_product(arr_1))
print(find_max_product(arr_2))