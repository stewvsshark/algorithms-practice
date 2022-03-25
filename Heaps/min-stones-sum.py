import heapq
import math

# You are given a 0-indexed integer array piles, where piles[i] represents the number of
#   stones in the ith pile, and an integer k. You should apply the following operation exactly k times:
#
# Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
# Notice that you can apply the operation on the same pile more than once.
#
# Return the minimum possible total number of stones remaining after applying the k operations.
#
# floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).


def min_stone_sum(piles, k):
    negative_piles = []
    for pile in piles:
        negative_piles.append(-pile)

    heapq.heapify(negative_piles)
    while k > 0:
        val = math.floor(heapq.heappop(negative_piles)/2)
        heapq.heappush(negative_piles, val)
        k -= 1

    piles_sum = 0
    for pile in negative_piles:
        piles_sum += -pile

    return piles_sum


test_piles_1 = [5,4,9]
test_k_1 = 2
print(min_stone_sum(test_piles_1, test_k_1))

test_piles_2 = [4,3,6,7]
test_k_2 = 3
print(min_stone_sum(test_piles_2, test_k_2))


