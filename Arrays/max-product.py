import math


def max_product(nums):
    first_largest, second_largest = -math.inf, -math.inf
    for num in nums:
        if num > first_largest:
            tmp = first_largest
            first_largest = num
            second_largest = tmp
        elif num > second_largest:
            second_largest = num

    return (first_largest-1) * (second_largest-1)



nums = [3,7]
print(max_product(nums))