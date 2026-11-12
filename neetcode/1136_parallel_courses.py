# https://leetcode.com/problems/parallel-courses/description/
# https://neetcode.io/solutions/parallel-courses
# Topological Sort: Kahn BFS

# relations[i] = [prevCoursei, nextCoursei].
# Must take prevCourse before nextCourse.

# Ex: 1   2  Directed graph. Arrows point top to bottom.
#      \ /
#       3
# n = 3 courses. relations = [[1,3],[2,3]]

# Use BFS, since we seek minimum # of semesters to take all courses.
# Each semester, take as many courses as you want. Each semester = 1 BFS level.

# See https://github.com/rayning0/ctci/blob/master/neetcode/210_course_schedule_ii.py as reference.

# BFS (Kahn Topological Sort).
# Time: O(V + E), Space: O(V + E)
# V = # of courses (nodes), E = # of prerequisites (edges)
from collections import deque
def minimumSemesters(n: int, relations: list[list[int]]) -> int:
    indegree = [0] * (n+1)  # Courses are from 1 to n (not 0 to n - 1)
    semesters = 0
    finished = 0

    graph = {course: [] for course in range(1, n+1)}
    for prevCourse, nextCourse in relations:
        graph[prevCourse].append(nextCourse)
        indegree[nextCourse] += 1

    q = deque()
    for course in range(1, n+1):
        if indegree[course] == 0:
            q.append(course)

    while q:
        size = len(q)

        for _ in range(size):
            prevCourse = q.popleft()
            finished += 1

            for nextCourse in graph[prevCourse]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    q.append(nextCourse)

        semesters += 1

    return semesters if finished == n else -1

if __name__ == '__main__':
    assert minimumSemesters(3, [[1,3],[2,3]]) == 2
    assert minimumSemesters(3, [[1,2],[2,3],[3,1]]) == -1
    print('All tests passed!')
