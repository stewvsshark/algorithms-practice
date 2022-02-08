
# You are given an array arr of N integers. For each index i,
#   you are required to determine the number of contiguous subarrays
#   that fulfill the following conditions:
#   1. The value at index i must be the maximum element in the contiguous subarrays, and
#   2. These contiguous subarrays must either start from or end on index i.

# Input constraints:
#   Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
#   Size N is between 1 and 1,000,000

# Key detail: the longest subarray must start or end at the index: so iterate forwards from the
#   beginning to the index, then backwards from the end to the index
# Key detail: The # of contiguous subarrays; not the length of the longest

# Look up:
# 1. enumerate(arr) allows you to iterate a list to get both the index and element
# 2. some_array = [element] * n initializes some_array of len(n) with element for each value
    # 3. set() creates a set; sets cannot hold arrays. type must be hashable (like a dictionary)
# 4. ranges are exclusive
#


# Questions:
# 1. What is a contiguous subarray?

# Optimizations:

# Runtime:

def count_subarrays(arr):
    n = len(arr)
    result = [1] * n
    for i, element in enumerate(arr):
        for direction in [1, -1]:
            step = 1
            while 0 <= i + direction * step < n and arr[i + direction * step] < element:
                result[i] += 1
                step += 1

    return result


def count_subarrays_with_stack(arr):
    n = len(arr)
    result = [n] * n
    st = []
    for i, x in enumerate(arr):
        while st and x >= arr[st[-1]]:
            result[st.pop()] -= n - i
        st.append(i)
    st.clear()
    for i, x in reversed(list(enumerate(arr))):
        while st and x >= arr[st[-1]]:
            result[st.pop()] -= i + 1
        st.append(i)
    return result


def my_implementation(arr):
    array_length = len(arr)
    result = [1] * array_length

    for i, element in enumerate(arr):
        sub_arrays = 0
        for j in range(i+1, array_length):
            if arr[i] > arr[j]:
                sub_arrays += 1
            else:
                break
        for k in range(i-1, -1, -1):
            if arr[i] > arr[k]:
                sub_arrays += 1
            else:
                break

        result[i] += sub_arrays

    return result







print(count_subarrays([3, 4, 1, 6, 2]))
print(my_implementation([3, 4, 1, 6, 2]))  # [1, 3, 1, 5, 1]
print(count_subarrays([2, 4, 7, 1, 5, 3]))
print(my_implementation([2, 4, 7, 1, 5, 3]))  # [1, 2, 6, 1, 3, 1]
