import heapq

# There is a school that has classes of students and each class will be having a final exam.
#   You are given a 2D integer array classes, where classes[i] = [passi, totali].
#   You know beforehand that in the ith class, there are totali total students,
#   but only passi number of students will pass the exam.
#
# You are also given an integer extraStudents. There are another extraStudents brilliant students that
#   are guaranteed to pass the exam of any class they are assigned to.
#   You want to assign each of the extraStudents students to a class in a way that maximizes the
#   average pass ratio across all the classes.
#
# The pass ratio of a class is equal to the number of students of the class that will pass the exam
#   divided by the total number of students of the class. The average pass ratio is the sum of pass
#   ratios of all the classes divided by the number of the classes.
#
# Return the maximum possible average pass ratio after assigning the extraStudents students.
#   Answers within 10^-5 of the actual answer will be accepted.

# Trick: heaping value - use the delta between the current ratio and ratio
#   resulting from adding an extra student

def max_average_ratio(classes, extra_students):
    h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
    heapq.heapify(h)
    while extra_students:
        v, a, b = heapq.heappop(h)
        a, b = a + 1, b + 1
        heapq.heappush(h, (-(a + 1) / (b + 1) + a / b, a, b))
        extra_students -= 1
    return sum(a / b for v, a, b in h) / len(h)


# print(max_average_ratio([[97,500],[30,915],[400,856],[444,623],[781,786],[3,713]], 8))
print (max_average_ratio([[1,2],[3,5],[2,2]], 2))