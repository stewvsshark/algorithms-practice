import heapq
import math

# You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
# It takes you 1 minute to eat all of the pieces of candy in a bag (regardless of how many pieces of candy are inside),
#   and as soon as you finish, the bag mysteriously refills.
# If there were x pieces of candy in the bag at the beginning of the minute,
#   then after you've finished you'll find that floor(x/2) pieces are now inside.
# You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

# Insights & approach
# - Is K relevant?
# - Max heap the list after eating, and continually eat from the arr[0] bag

#

def max_candies(arr, k):
    candies_consumed = 0
    arr_len = len(arr)
    while k > 0:
        arr = heapq.nlargest(arr_len, arr)
        candies_consumed += arr[0]
        arr[0] = math.floor(arr[0]/2)
        k -= 1

    return candies_consumed


arr_1 = [2, 1, 7, 4, 2]  # 14
print(max_candies(arr_1, 3))
arr_2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]  # 228
print(max_candies(arr_2, 3))
