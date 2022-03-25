import collections

# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a
#   different task. Tasks could be done in any order. Each task is done in one unit of time.
#   For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks
#   (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#   The cool down period can either be filled with other tasks, or can just be idle time if no other tasks exist
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.
# Constraints:
#   1 <= task.length <= 10^4
#   tasks[i] is upper-case English letter.
#   The integer n is in the range [0, 100].
import heapq


def least_interval(tasks, n):
    if n == 0:
        return len(tasks)
    task_count = {}
    for task in tasks:
        if task in task_count:
            task_count[task] -= 1
        else:
            task_count[task] = -1
    tasks_tuples = [(v, k) for k, v in task_count.items()]

    heapq.heapify(tasks_tuples)
    output_task_list = []
    while len(tasks_tuples) > 0:
        tmp_n = n+1
        tmp_tasks = []
        while tmp_n > 0:
            if len(tasks_tuples) == 0:
                output_task_list.append('idle')
            else:
                current_task = heapq.heappop(tasks_tuples)
                output_task_list.append(current_task[1])
                if current_task[0] < -1:
                    tmp_tasks.append((current_task[0]+1, current_task[1]))
            tmp_n -= 1
        for task in tmp_tasks:
            heapq.heappush(tasks_tuples, task)

    output_len = len(output_task_list)
    looper = True
    while looper:
        if output_task_list[output_len-1] == 'idle':
            output_task_list = output_task_list[:-1]
            output_len = len(output_task_list)
        else:
            looper = False

    print(output_task_list)
    return len(output_task_list)



#test_tasks_1 = ["A","A","A","A","A","A","B","C","D","E","F","G"]
test_n_1 = 2
# print(least_interval(test_tasks_1, test_n_1))

test_tasks_2 = ['A', 'A', 'A', 'B', 'B', 'B']
test_n_2 = 2
print(least_interval(test_tasks_2, test_n_1))


# Alternate Solution
def least_interval_alternate(tasks, n):
    maxFreq = 0
    max_count = 0
    dic = {}
    for task in tasks:
        if task in dic:
            dic[task] += 1
        else:
            dic[task] = 1
        if dic[task] > maxFreq:
            maxFreq = dic[task]
            max_count = 1
        elif dic[task] == maxFreq:
            max_count += 1

    if len(dic) <= n+1:
        return (maxFreq-1) * (n+1) + max_count
    else:
        return max((maxFreq-1) * (n+1) + max_count, len(tasks))