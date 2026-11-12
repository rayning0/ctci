# https://leetcode.com/problems/course-schedule-ii/description/
# https://neetcode.io/solutions/course-schedule-ii
# Topological Sort: Kahn BFS/DFS Cycle Detection

# Topological sort: ordering of all vertices in a directed graph so that, for each directed edge A → B, vertex A appears before vertex B.
# Here, every prereq must appear before the course that depends on it: (prereq -> course)

# DFS: Recursively explore each course's prereqs. Append a course to order only after all its prereqs have been explored.
# BFS: Kahn algorithm starts with courses with 0 prereqs (indegree == 0). Once a course is done, drop outstanding
# prereq counts (indegree) of courses that depend on it. Add course to queue only when its indegree == 0

# 1. Which courses to take first? DFS solution stored "course → prerequisites", but
# Kahn's algorithm does opposite: "prerequisite → courses unlocked by completing it."

# 2. For each course, number of prerequisites it still needs
# is "indegree" = number of incoming edges.

# Add all courses with indegree of 0 (no prereqs) to queue!

# Ex: (from Test #1). This is DIRECTED graph. All arrows point from top to bottom.
#     0    1
#      \  /
#       2
#      /  \
#     3    4
#      \  /
#       5
# indegree = [0,0,2,1,1,2]
# indegree[0] == 0 and indegree[1] == 0 since courses 0,1 have 0 prereqs.
# indegree[2] == 2 since course 2 has 2 prereqs, etc.

# 3. After finish each course, drop its indegree value by 1.

# Ex: course 2 has 2 prereqs, 0 and 1. indegree[2] == 2.
# When finish course 0, indegree[2] -= 1.
# When finish course 1, indegree[2] -= 1 again. Now indegree[2] == 0.

# If indegree of course == 0 (no more prereqs), add that course to queue.

# 4. How to find cycles?
# In cycle, each course has at least 1 prerequisite. None will ever reach indegree == 0.
# If we finish processing queue, but some courses have indegree > 0, we have a cycle!
# If we successfully schedule all courses (all have indegree 0 and got added to queue), we had NO cycles.

# 1. Kahn Topological Sort (BFS)
# Time: O(V + E), Space: O(V + E)
# V = # of courses (nodes), E = # of prerequisites (edges)
from collections import deque
def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    indegree = [0] * numCourses
    graph = {course: [] for course in range(numCourses)}
    order = []

    # map each prereq to all its later courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

# Example: Test #1. DIRECTED graph. All arrows point from top to bottom.
# graph: {0: [2], 1: [2], 2: [3, 4], 3: [5], 4: [5], 5: []}
# indegree: [0, 0, 2, 1, 1, 2]
#     0    1
#      \  /
#       2
#      /  \
#     3    4
#      \  /
#       5

    q = deque()
    # add all courses with 0 prereqs to queue
    for course, deg in enumerate(indegree):
        if deg == 0:
            q.append(course)

    # BFS
    while q:
        prereq = q.popleft()
        order.append(prereq)

        for course in graph[prereq]:
            indegree[course] -= 1
            if indegree[course] == 0:
                q.append(course)

    # if we successfully schedule all courses, return order, else we failed
    return order if len(order) == numCourses else []
    # for deg in indegree:
    #     if deg > 0:     # we have cycle
    #         return []
    # return order

# 2. DFS Topological Sort
# Almost same as LC 207 (Course Schedule): https://github.com/rayning0/ctci/blob/master/neetcode/207_course_schedule.py
# Time: O(V + E), Space: O(V + E)
# V = # of courses (nodes), E = # of prerequisites (edges)
def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    visited = set()
    no_cycles = set()
    order = []

    pmap = {course: [] for course in range(numCourses)}
    # map each course to its prereqs
    for course, prereq in prerequisites:
        pmap[course].append(prereq)

    # DFS
    def is_cycle(course):
        if course in no_cycles:
            return False

        visited.add(course)

        for prereq in pmap[course]:
            if prereq in visited or is_cycle(prereq):
                return True

        visited.remove(course)  # Backtrack
        no_cycles.add(course)
        order.append(course)
        return False

    for course in range(numCourses):
        if is_cycle(course):
            return []
    return order

# Why do we need the list "order"? Can't we use set "no_cycles" in its place?
# No, sets do not keep insertion order!
# Ex: numCourses = 3, prerequisites = [[0,2], [2,1]]. Answer = [1,2,0]
# If we create set = {1,2,0}, Python automatically reorders it to {0,1,2}.

if __name__ == '__main__':
    assert findOrder(6, [
        [2, 0],
        [2, 1],
        [3, 2],
        [4, 2],
        [5, 3],
        [5, 4],
    ]) == [0,1,2,3,4,5]
    assert findOrder(2, [[1,0]]) == [0,1]
    assert findOrder(3, [[1,0]]) == [0,2,1] # or [0,1,2] or [2,0,1]. All that matters: 0 is before 1.
    assert findOrder(3, [[0,1],[1,2],[2,0]]) == []              # cycle
    assert findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]
    assert findOrder(3, [[0, 2], [2, 1]]) == [1,2,0]
    assert findOrder(1, []) == [0]
    # 12 courses and 19 prerequisite relationships. Has several prerequisites a course,
    # branching paths, and a course with no dependencies.
    assert findOrder(12, [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2],
        [4, 1],
        [5, 2],
        [5, 3],
        [6, 3],
        [6, 4],
        [7, 4],
        [7, 5],
        [8, 5],
        [8, 6],
        [9, 6],
        [9, 7],
        [10, 7],
        [10, 8],
        [11, 9],
        [11, 10],
    ]) == [0, 1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11]
    # # 12 courses, 20 prerequisite relationships, and multiple cycles.
    assert findOrder(12, [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2],
        [4, 1],
        [5, 2],
        [5, 3],
        [6, 3],
        [6, 4],
        [7, 4],
        [7, 5],
        [8, 5],
        [8, 6],
        [9, 6],
        [9, 7],
        [10, 7],
        [10, 8],
        [11, 9],
        [11, 10],
        [3, 9],
    ]) == []    # cycle
    print('All tests passed!')

# ----Output for Kahn Topological Sort (BFS)----
# graph: {0: [2], 1: [2], 2: [3, 4], 3: [5], 4: [5], 5: []}
# indegree: [0, 0, 2, 1, 1, 2]
# order: [0, 1, 2, 3, 4, 5]

# graph: {0: [1], 1: []}
# indegree: [0, 1]
# order: [0, 1]

# graph: {0: [1], 1: [], 2: []}
# indegree: [0, 1, 0]
# order: [0, 2, 1]

# graph: {0: [2], 1: [0], 2: [1]}
# indegree: [1, 1, 1]
# has cycle

# graph: {0: [1, 2], 1: [3], 2: [3], 3: []}
# indegree: [0, 1, 1, 2]
# order: [0, 1, 2, 3]

# graph: {0: [], 1: [2], 2: [0]}
# indegree: [1, 0, 1]
# order: [1, 2, 0]

# graph: {0: []}
# indegree: [0]
# order: [0]

# graph: {0: [1, 2], 1: [3, 4], 2: [3, 5], 3: [5, 6], 4: [6, 7], 5: [7, 8], 6: [8, 9], 7: [9, 10], 8: [10], 9: [11], 10: [11], 11: []}
# indegree: [0, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2]
# order: [0, 1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11]

# graph: {0: [1, 2], 1: [3, 4], 2: [3, 5], 3: [5, 6], 4: [6, 7], 5: [7, 8], 6: [8, 9], 7: [9, 10], 8: [10], 9: [11, 3], 10: [11], 11: []}
# indegree: [0, 1, 1, 3, 1, 2, 2, 2, 2, 2, 2, 2]
# has cycle

# ----pmap for each test----
# {0: [], 1: [], 2: [0, 1], 3: [2], 4: [2], 5: [3, 4]}
# {0: [], 1: [0]}
# {0: [], 1: [0], 2: []}
# {0: [1], 1: [2], 2: [0]}
# {0: [], 1: [0], 2: [0], 3: [1, 2]}
# {0: [2], 1: [], 2: [1]}
# {0: []}
# {0: [], 1: [0], 2: [0], 3: [1, 2], 4: [1], 5: [2, 3], 6: [3, 4], 7: [4, 5], 8: [5, 6], 9: [6, 7], 10: [7, 8], 11: [9, 10]}
# {0: [], 1: [0], 2: [0], 3: [1, 2, 9], 4: [1], 5: [2, 3], 6: [3, 4], 7: [4, 5], 8: [5, 6], 9: [6, 7], 10: [7, 8], 11: [9, 10]}

# ----------------------------------------------------------------------------------------------
                                                    Topological Sort
                                DFS 	                                    Kahn BFS
Graph direction         Course -> Prereqs                           Prereq -> Later courses
Core idea	            Explore prerequisites recursively	        Process courses with 0 outstanding prereqs
Starting point          Any course                                  Courses with indegree == 0
Cycle detected when	    See course in visited()	                    Queue empties before all nodes processed. Not all courses processed.
Main structures	        visited(), no_cycles(), order[]	            indegree[], graph = {}, queue, order[]
When to append to order After recursively finishing prereqs         When removing course from queue
Time	                O(V+E)                                      O(V+E)
Space                   O(V+E)                                      O(V+E)
Python recursion limit	Potential issue	                            None
Natural application	    Dependency traversal, cycle detection	    Scheduling, dependency resolution
