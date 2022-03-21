import heapq

# You are given an integer array score of size n, where score[i] is the score of the ith athlete
#   in a competition. All the scores are guaranteed to be unique.
#
# The athletes are placed based on their scores, where the 1st place athlete has the highest score,
#   the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
#
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number
#   (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.


def find_relative_ranks(score):
    n = len(score)
    score_heap = score.copy()
    answer = [-1] * n
    heapq.heapify(score_heap)
    i = n
    while i >= 1:
        val = heapq.heappop(score_heap)
        score_index = score.index(val)
        if i > 3:
            answer[score_index] = str(i)
        elif i == 1:
            answer[score_index] = "Gold Medal"
        elif i == 2:
            answer[score_index] = "Silver Medal"
        elif i == 3:
            answer[score_index] = "Bronze Medal"
        i -= 1

    return answer


test_scores = [5,4,3,2,1]
print(find_relative_ranks(test_scores))
