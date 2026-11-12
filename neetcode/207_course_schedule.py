# https://leetcode.com/problems/course-schedule/description/
# https://neetcode.io/solutions/course-schedule
# DFS (or use Kahn Topological Sort/Cycle Detection)

# prerequisites[i] = [ai, bi]. Must take course bi first to take course ai.
# This is a DIRECTED graph. bi -> ai.

# *** This problem doesn't require only 1 root or a connected graph.
# It only requires the directed prerequisite graph has NO CYCLES! ***

# Make adjacency list. key = course, value = list of prereqs for course.
# pmap = {
#     0: [],
#     1: [0],
#     2: [0],
#     3: [1,2],
#     4: [2],
#     5: [3,4],
#     ...
# }

# In checking prereqs, how do we distinguish between course we already
# finished checking vs. a course still being explored in current DFS path?

# DFS
# Time: O(V + E), Space: O(V + E)
# V = # of courses (nodes), E = # of prerequisites (edges)
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    visited = set()     # courses on current DFS path
    no_cycles = set()   # courses whose whole prerequisite paths have no cycles

    pmap = {course: [] for course in range(numCourses)}
    for course, prereq in prerequisites:
        pmap[course].append(prereq)

    # DFS
    # Found cycle in course prerequisite path? Then we can't finish courses.
    def is_cycle(course):
        if course in no_cycles: # Memoization. Don't recheck courses we already found with no cycles!
            return False

        visited.add(course)

        for prereq in pmap[course]:
            if prereq in visited or is_cycle(prereq):
                return True

        visited.remove(course)  # Backtrack after checking all prereqs.
        no_cycles.add(course)   # Memoization
        return False

    for course in range(numCourses):
        if is_cycle(course):
            return False
    return True

# Why backtrack after for loop instead of inside it? A course must stay in visited set()
# till all its prereqs get checked, for full lifetime of its DFS call.
# Ex: pmap = {
#     0: [],
#     1: [0],
#     2: [0, 1]
# }

# 2 stays in visited throughout both DFS branches, since dfs(2) is still active.
# But 0 is removed as soon as its own DFS call finishes.

# dfs(2)            visited = {2}
#   |
#   ├── dfs(0)      visited = {2, 0}
#   |   └── done    visited = {2}
#   |
#   └── dfs(1)      visited = {2, 1}
#       |
#       └── dfs(0)  visited = {2, 1, 0}
#           └── done

if __name__ == '__main__':
    assert canFinish(2, [[1,0]]) is True            # no cycle
    assert canFinish(2, [[1,0],[0,1]]) is False     # cycle
    assert canFinish(8, prerequisites = [           # no cycle
        [1, 0], # root course 0
        [2, 1],
        [3, 2],
        [5, 4], # root course 4
        [6, 5],
        [7, 6]
    ]) is True
    assert canFinish(8, prerequisites = [           # no cycle
        [2, 0], # root course 0
        [2, 1], # root course 1
        [3, 1],
        [4, 2],
        [4, 3],
        [5, 4],
        [6, 0],
        [7, 5],
        [7, 6]
    ]) is True
    assert canFinish(9, prerequisites = [           # cycle [5 -> 6 -> 7 -> 5]
        [1, 0], # root course 0
        [2, 1],
        [3, 2],
        [5, 4], # root course 4
        [6, 5],
        [7, 6],
        [5, 7]
    ]) is False # root course 8 (has no prereqs)
    assert canFinish(12, [                          # cycle
        [1, 0],
        [2, 0],
        [3, 1],
        [4, 2],
        [5, 3],
        [5, 4],
        [6, 5],
        [7, 6],
        [8, 7],
        [9, 8],
        [10, 9],
        [11, 10],
        [4, 8],
        [7, 2]
    ]) is False
    print('All tests passed!')

# pmap for above 6 tests
# {0: [], 1: [0]}
# {0: [1], 1: [0]}
# {0: [], 1: [0], 2: [1], 3: [2], 4: [], 5: [4], 6: [5], 7: [6]}
# {0: [], 1: [], 2: [0, 1], 3: [1], 4: [2, 3], 5: [4], 6: [0], 7: [5, 6]}
# {0: [], 1: [0], 2: [1], 3: [2], 4: [], 5: [4, 7], 6: [5], 7: [6], 8: []}
# {0: [], 1: [0], 2: [0], 3: [1], 4: [2, 8], 5: [3, 4], 6: [5], 7: [6, 2], 8: [7], 9: [8], 10: [9], 11: [10]}
