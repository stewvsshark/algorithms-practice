
# Given a list of n integers arr[0..(n-1)],
#   determine the number of different pairs of elements within it which sum to k.
# If an integer appears in the list multiple times, each copy is considered to be different;
#   that is, two pairs are considered different if one pair includes at least one array index
#   which the other doesn't, even if they include the same values.

# Possible optimizations:
# 1. Sort the list ahead of time - order is not of importance?

# Lookups:
# 1. arr.sort() sorts in place

def number_of_ways(arr, k):
    array_length = len(arr)
    result = 0
    for i in range(array_length):
        for j in range(i+1, array_length):
            if (arr[i] + arr[j]) == k:
                result += 1

    return result


def moreEfficient(arr, k):
    array_length = len(arr)
    result = 0
    arr.sort()
    i, j = 0, (array_length-1)
    while i < j:
        pair_sum = arr[i] + arr[j]
        if pair_sum == k:
            i_start_val = arr[i]
            j_start_val = arr[j]
            i_start_index = i
            j_start_index = j
            if i_start_val == j_start_val:
                while i <= j:
                    i += 1
                    result += 1
            else:
                print()
                # figure out how to count occurrences

        elif pair_sum > k:
            j -= 1
        else:
            i += 1

    return result


print(number_of_ways([1, 2, 3, 4, 3], 6))  # 2
print(moreEfficient([1, 2, 3, 4, 3], 6))
print(number_of_ways([1, 5, 3, 3, 3], 6))  # 4
print(moreEfficient([1, 5, 3, 3, 3], 6))

