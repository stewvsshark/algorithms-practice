
# Given a sequence of n integers arr, determine the lexicographically smallest sequence which
#   may be obtained from it after performing at most k element swaps, each involving a pair of
#   consecutive elements in the sequence.
# Note: A list x is lexicographically smaller than a different equal-length list y if and only if,
#   for the earliest index at which the two lists differ, x's element at that index is smaller than y's
#   element at that index.

# Questions/Insights:
# 1. Does the list contain strictly distinct integers
# 2. Key detail: CONSECUTIVE swaps
# 3. Assume k < N?

def find_min_array(arr, k):
    i = 0
    while k > 0:
        min_index = arr.index(min(arr[i:k+1]))
        swaps = 0
        while min_index > i:
            tmp = arr[min_index]
            arr[min_index] = arr[min_index-1]
            arr[min_index-1] = tmp
            min_index -= 1
            swaps += 1
        k -= swaps
        i += 1
    return arr

arr_1 = [5, 3, 1]
print(find_min_array(arr_1, 2))
arr_2 = [8, 9, 11, 2, 1]
print(find_min_array(arr_2, 3))
