# https://leetcode.com/problems/task-scheduler/description/
# https://neetcode.io/solutions/task-scheduler
# Max Heap + Queue. Should be HARD, not Medium!

# max heap = tasks ready to run now:    (-count, task)
# queue    = tasks not ready now:       (ready_time, remaining_count, task)

# Make "ready", max heap of tasks by remaining count.
# Loop while "ready" or "cooling":
# 1. If no tasks ready, jump to next ready_time: cooling[0][0]
# 2. Run most frequent ready task.
# 3. If task has any remaining counts, add it to "cooling" queue.
# 4. While tasks at head of "cooling" queue are ready, pop them, then push them back on "ready" heap.

import heapq
from collections import deque, Counter

# Time: O(m), Space: O(1) <--- since we have at most 26 distinct tasks (A-Z)
# m = len(tasks)
def leastInterval(tasks: list[str], n: int) -> int:
    # freq = Counter(tasks), or:
    # for task in tasks:
    #     freq[task] = freq.get(task, 0) + 1

    ready = []          # max heap = tasks ready to run now:    (-count, task)
    cooling = deque()   # queue    = tasks not ready now:       (ready_time, remaining_count, task)
    time = 0

    # MAX HEAP: tasks ready to run NOW.
    # To run tasks with max freq first, use max heap.
    for task, count in Counter(tasks).items():
        heapq.heappush(ready, (-count, task))

    while ready or cooling:
        # If no tasks ready to run, jump to next time a task is ready.
        if not ready:
            time = cooling[0][0]
        else:
            time += 1

            # Run most frequent ready task. Pop it from max heap.
            remain, task = heapq.heappop(ready)
            # Since remain count < 0, decrease count by adding 1. (Moves it closer to 0.)
            remain += 1

            # Still have more copies of this task? (remaining count != 0)
            if remain:
                ready_time = time + n   # earliest next time task can run

                # QUEUE: tasks not ready now
                cooling.append((ready_time, remain, task))

        # Are any tasks at front of cooling queue ready to run?  (ready_time == current time)
        while cooling and cooling[0][0] == time:
            # Pop them from queue, then push their remaining count back on ready heap.
            _, remain, task = cooling.popleft()
            heapq.heappush(ready, (remain, task))

    return time     # total processing time


if __name__ == "__main__":
    assert leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert leastInterval(["A","C","A","B","D","B"], 1) == 6
    assert leastInterval(["A","A","A","B","B","B"], 3) == 10
    assert leastInterval(["X","X","Y","Y"], 2) == 5
    assert leastInterval(["A","A","A","B","C"], 3) == 9
    print("All tests passed!")

# ["A","A","A","B","B","B"], n = 2
# freq = {A: 3, B: 3}
# run = [A, B, Idle, A, B, Idle, A, B]. len(run) == 8

# ["A","C","A","B","D","B"], n = 1
# freq = {A: 2, B: 2, C: 1, D: 1}
# run = [A, B, A, B, C, D]. len(run) == 6.

# ["A","A","A","B","C"], n = 3
# freq = {'A': 3, 'B': 1, 'C': 1}
# run = [A, B, C, Idle, A, Idle, Idle, Idle, A]. len(run) = 9

# Time  Heap (ready)      Queue (cooling)                     Run
#       count, task       (ready_time, remain_count, task)

# 0     A3 B1 C1          -

# 1     B1 C1             A2@5: [(5, -2, A)]                  A

# 2     C1                A2@5                                B

# 3     -                 A2@5                                C

# 4     -                 A2@5                                Idle

# 5     A2                -                                   A
#       run A
#       ↓
#       -                 A1@9: [(9, -1, A)]

# 6     -                 A1@9                                Idle

# 7     -                 A1@9                                Idle

# 8     -                 A1@9                                Idle

# 9     A1                -                                   A
#       run A
#       ↓
#       -                 -
________________
Sample script for interview:

"We have tasks that can repeat, and after executing one task, we have to wait n intervals before executing the same task again."

"My goal is to keep the CPU busy whenever possible and minimize idle time."

Step 1: Frequency map
"The first thing I want to know is how many times each task still needs to run."

A:3
B:1
C:1
"I'll count frequency of each task."

Step 2: Which task should I run?
"Suppose several tasks are available. Which one should I choose?"

"Intuitively, the task with the highest remaining frequency is the hardest one to schedule because it has the most future cooldowns."

"So I'll always run the most frequent available task."

"So I'd use a max heap."

Step 3: Cooldown
"After I run a task, I can't immediately put it back into the heap because it's cooling down."

"So I need another data structure for tasks that aren't ready yet."

"A queue works well, because tasks become ready in chronological order."

Step 4: Simulation
"Now I can simulate time."

At each time unit:
1. "Run the most frequent ready task."
2. "Decrease its remaining count."
3. "If it still has remaining work, put it into the cooldown queue."
4. "Whenever a task finishes cooling down, move it back into the heap."

Step 5: Idle time
"Sometimes every remaining task is cooling down."

"If the heap is empty but the queue isn't, the CPU has to be idle."

"Instead of simulating every idle interval 1 by 1, jump directly to the next time a task becomes available."

Complexity
"Each execution of a task enters and leaves the heap once."

"So the running time is linear in the number of task executions, with heap operations over at most 26 task types."
