
# There are n students, numbered from 1 to n, each with their own yearbook.
# They would like to pass their yearbooks around and get them signed by other students.
# You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n
#   (in other words, it includes the integers from 1 to n exactly once each, in some order).
# The meaning of this list is described below.
# Initially, each student is holding their own yearbook.
# The students will then repeat the following two steps each minute: Each student i will first
#   sign the yearbook that they're currently holding (which may either belong to themselves or to another student),
#   and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i,
#   in which case student i will pass their yearbook back to themselves.
# Once a student has received their own yearbook back, they will hold on to it
#   and no longer participate in the passing process.
# It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook
#   back and will never end up holding more than one yearbook at a time.
# You must compute a list of n integers output, whose element at i-1 is equal to the number of
#   signatures that will be present in student i's yearbook once they receive it back.

# Look ups
# 1. if x in thing

# Questions
# 1. This detail is unclear to me: 'It's possible that arr[i-1] = i for any given i,
#   in which case student i will pass their yearbook back to themselves'

# Insights
# Consider that each student is a member of a single yearbook passing cycle.
#   For example, for input [3, 2, 4, 1], there are two yearbook passing cycles: {3, 4, 1} and {2}.
#   Therefore, the number of signatures for each member of a passing cycle is equal to the size of the cycle.
#   In the example, students {3, 4, 1} each get 3 signatures (1 for his/her self, and 1 for the other 2 students),
#   and student {2} gets 1 signature, his/her own signature.
#
# Student # 3 is in seat # 0 : Will always pass yearbook to seat # 2 (which is Student # 4)
# Student # 2 is in seat # 1 : Will always pass yearbook to seat # 1 (which is Student # 2)
# Student # 4 is in seat # 2 : Will always pass yearbook to seat # 3 (which is Student # 1)
# Student # 1 is in seat # 3 : Will always pass yearbook to seat # 0 (which is Student # 3)
#
# If you follow the groups' path, you will begin to see the "cycles", or roadmap of where yearbooks will be passed.
#   St#3 --> St#4 --> St#1 --> St#3
#   St#2 --> St#2

# Optimizations


# arr_3 = [3, 2, 4, 1]
def find_signature_counts(arr):
    arr_len = len(arr)  # 4
    visited_students = set()  # []
    signatures = [0] * arr_len  # [0, 0, 0, 0]
    root_indexes = [-1] * arr_len # [-1, -1, -1, -1]

    for i in range(arr_len):  # 0 -> 1
        student = arr[i]  # student = 3 -> 2
        if student in visited_students:  # []
            continue
        else:
            visited_students.add(student)  # [3] -> [3, 4, 1, 2]

        # consider the current student to be the root of a cycle, and traverse back to itself
        signatures[i] = 1   # [1, 0, 0, 0] -> [3, 1, 0, 0]
        next_i = student - 1  # 2 -> 1
        while next_i != i:  # 2 != 0 -> 3 != 0 -> 0 == 0 1 == 1
            signatures[i] += 1  # [2, 0, 0, 0] -> [3, 0, 0, 0]
            root_indexes[next_i] = i  # [-1, -1, 0, -1] -> [-1, -1, 0, 0]
            visited_students.add(arr[next_i])  # [3, 4] -> [3, 4, 1]
            next_i = arr[next_i] - 1  # 3 -> 1 - > 0

    for i in range(arr_len):
        if root_indexes[i] != -1:  # 0: -1 == 1 -> 1: -1 == -1 -> 2: 0 != -1 -> 3: 0 != -1
            signatures[i] = signatures[root_indexes[i]]  # [3, 1, 3, 0] -> [3, 1, 3, 3]
    return signatures


arr_1 = [2, 1]
arr_2 = [1, 2]
arr_3 = [3, 2, 4, 1]

# print(find_signature_counts(arr_1))
# print(find_signature_counts(arr_2))
print(find_signature_counts(arr_3))
