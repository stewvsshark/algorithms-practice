
# Suppose we have a list of N numbers, and repeat the following operation until we're left with
#   only a single number: Choose any two numbers and replace them with their sum.
# Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty
#   for the entire list as the sum of the penalties of each operation.
# For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation,
#   which would transform the list into [1, 5, 4, 5] and incur a penalty of 5.
# The goal in this problem is to find the highest possible penalty for a given input.

def get_total_time(arr):
    result = do_greedy(arr, 0)
    return result


def do_greedy(arr, result):
    if len(arr) == 1:
        return 0
    else:
        arr.sort()
        greedy_sum = arr[len(arr)-1] + arr[len(arr)-2]
        new_arr = arr[:-2] + [greedy_sum]
        return greedy_sum + do_greedy(new_arr, result)


arr_1 = [4, 2, 1, 3]
print(get_total_time(arr_1))
arr_2 = [2, 3, 9, 8, 4]
print(get_total_time(arr_2))
