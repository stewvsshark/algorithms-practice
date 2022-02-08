import heapq
import math

# You're given a list of n integers arr[0..(n-1)].
# You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive),
#   output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
# The median of a list of integers is defined as follows. If the integers were to be sorted, then:
#   If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
#   Otherwise, if there are an even number of integers, then the median is equal to the average of the two
#   middle-most integers in the sorted order.

# Example
# n = 4
# arr = [5, 15, 1, 3]
# output = [5, 10, 5, 4]

# Insights & approach:
# - n < len(arr)
# - min heap the arr[0..i] subarray
# -     if len(subarray) % 2 = 1 take subarray[floor(len/2)] as median
# -     if len(subarray) % 2 = 0 take mean(subarray[len/2], subarray[(len/2)+1]

# Lookups:
# 1. range(start, stop, step)

# Questions
# 1. Does the mean have to be an integer? -> answered in description

# Optimizations
# 1. Reuse max-heaped subarray

def find_median(arr):
    arr_length = len(arr)
    result = [0] * arr_length
    result[0] = arr[0]
    sub_arr = []
    sub_arr.insert(0, arr[0])
    for i in range(1, arr_length, 1):
        sub_arr.insert(i, arr[i])
        sub_arr_len = i + 1

        # reuse sorted max-heaped array
        sub_arr = heapq.nsmallest(sub_arr_len, sub_arr)

        if sub_arr_len % 2 == 0:
            upper_index = sub_arr_len//2
            lower_index = upper_index - 1
            median = math.floor((sub_arr[upper_index] + sub_arr[lower_index]) / 2)
        else:
            middle_index = math.floor(sub_arr_len/2)
            median = (sub_arr[middle_index])
        result[i] = median
    return result


arr_1 = [5, 15, 1, 3]  # [5, 10, 5, 4]
arr_2 = [2, 4, 7, 1, 5, 3]  # [2, 3, 4, 3, 4, 3]

print(find_median(arr_1))
print(find_median(arr_2))