import heapq

def reorganize_string(s):
    n=1
    task_count = {}
    for task in s:
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

    if 'idle' in output_task_list:
        return ""
    else:
        return ''.join(output_task_list)


print(reorganize_string("aab"))