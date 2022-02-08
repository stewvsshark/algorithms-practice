
# Given two arrays A and B of length N, determine if there is a way to make A equal to B by
#   reversing any subarrays from array B any number of times.

# Looked up
# 1. dict.fromkeys(my_arr, initial_val)

# Insights
# 1. Lengths must be equal
# 2. We don't have to actually figure out the solution, just if it's possible

# Questions
# 1. We don't actually need to construct the original array, just see if it's possible?
# 2. Subarray can mean any length? 0 < n < max_int?

# Optimizations


def are_they_equal(array_a, array_b):
    dict_b = dict.fromkeys(array_b, 1)

    for element in array_a:
        if dict_b.get(element):
            continue
        else:
            return False

    return True


a_1 = [1, 2, 3, 4]
b_1 = [1, 4, 3, 2]
print(are_they_equal(a_1, b_1))

a_2 = [1, 2, 3, 4]
b_2 = [1, 2, 3, 5]
print(are_they_equal(a_2, b_2))


