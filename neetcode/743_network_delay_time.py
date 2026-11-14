# https://leetcode.com/problems/network-delay-time/description/
# https://neetcode.io/solutions/network-delay-time
# Dijkstra shortest path

# times[i] = (ui, vi, wi). ui = source node, vi = target node, wi = travel time from source to target.
# Send signal from node k. Return min time for all n nodes to get the signal. If impossible for all nodes, return -1.

# Use a min heap (not queue) to process nodes by shortest travel time first! (time, node)
# But overall algorithm still looks generally like BFS.

# <Make weighted adjacency list>
# Ex: times = [[2,1,1],[2,3,1],[3,4,1]]
# graph = {
#     1: [],
#     2: [(1,1), (3,1)],  <--- u: [(v1, w1), (v2, w2), ...] or source: [(target1, time1), (target2, time2), ...]
#     3: [(4,1)],
#     4: [],
# }

# <Track min arrival time>
# min_time[v] = min travel time from nodes k to v, so far. May update later.

import heapq
# Time: O(V + E log V), Space: O(V + E)
# V = n, E = len(times)
def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    # Make weighted adjacency list
    # graph = {source: [(target1, time1), (target2, time2), ...]}
    graph = {source: [] for source in range(1, n + 1)}
    for source, target, time in times:
        graph[source].append((target, time))

    min_time = [float('inf')] * (n + 1)   # set initial times from k to all nodes to infinity
    min_time[k] = 0                       # starting node (k) travel time is 0

    # min heap processes nodes by shortest travel time first: (time, node)
    heap = [(0, k)]     # start signal from node k
    while heap:
        source_time, source = heapq.heappop(heap)

        # Stale-Entry Skipping: skip paths with longer time to source than current min_time.
        if source_time > min_time[source]:
            continue

        for target, target_time in graph[source]:               # explore neighbors of source
            new_target_time = source_time + target_time

            # Relaxation: update neighbor only when you find shorter path
            if new_target_time < min_time[target]:
                min_time[target] = new_target_time              # update shortest known travel time to target
                heapq.heappush(heap, (new_target_time, target)) # push better routes on heap

    # for nodes 1 to n (ignore node 0), max value is shortest time for all n nodes to get the signal!
    delay = max(min_time[1:])

    # if a node still has initial infinity time, we never reached it, so return -1.
    return -1 if delay == float('inf') else delay

if __name__ == '__main__':
    assert networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2

# graph: {1: [], 2: [(1, 1), (3, 1)], 3: [(4, 1)], 4: []}
# heap: [(1, 1)]
# heap: [(1, 1), (1, 3)]
# heap: [(2, 4)]
# delay: 2. min_time: [inf, 1, 0, 1, 2]

    assert networkDelayTime([[1,2,1]], 2, 1) == 1
    assert networkDelayTime([[1,2,1]], 2, 2) == -1
    assert networkDelayTime([[1,2,1],[2,3,1],[1,4,4],[3,4,1]], 4, 1) == 3

# graph: {1: [(2, 1), (4, 4)], 2: [(3, 1)], 3: [(4, 1)], 4: []}
# heap: [(1, 2)]
# heap: [(1, 2), (4, 4)]
# heap: [(2, 3), (4, 4)]
# heap: [(3, 4), (4, 4)]
# delay: 3. min_time: [inf, 0, 1, 2, 3]

    assert networkDelayTime([[1,2,1],[2,3,1]], 3, 2) == -1
    assert networkDelayTime([[1, 2, 1], [1, 2, 2]], 3, 1) == -1

# graph: {1: [(2, 1), (2, 2)], 2: [], 3: []}
# heap: [(1, 2)]
# delay: inf. min_time: [inf, 0, 1, inf]

    assert networkDelayTime([[1, 2, 10], [1, 3, 1]], 3, 1) == 10

# graph: {1: [(2, 10), (3, 1)], 2: [], 3: []}
# heap: [(10, 2)]
# heap: [(1, 3), (10, 2)]
# delay: 10. min_time: [inf, 0, 10, 1]
    print('All tests passed!')

# Why is time complexity O(V + E log V)?
# - To push/pop on a heap: O(log E) time. Do it for E edges. Total heap operations: O(E log E).
# - Make adjacency list + add edges: O(V + E)

# Total: O(V + E + E log E) = O(V + E log E)
# Since E <= V(V - 1), taking log of both sides gives: O(log E) = O(log V^2) = O(2 log V) = O(log V).
# O(V + E log E) = O(V + E log V)


-------------- <Dijkstra shortest path algorithm> --------------

Dijkstra's algorithm solves the single-source shortest-path problem:
Given a weighted graph and starting node, find minimum total edge weight required to reach every other reachable node. It works for directed/undirected graphs, but requires all edge weights >= 0.

Central idea: GREEDY selection + relaxation
Dijkstra repeatedly selects the node with the smallest tentative distance.

Once that node is selected with its current best distance, that distance is guaranteed to be optimal (assuming all edge weights >= 0).

Then it explores outgoing edges to see if it can improve distances to neighboring nodes.

Make weighted adjacency list:
graph = {start: [(end1, weight1), (end2, weight2), ...]}

dist = [float('inf')] * (n + 1)   # set initial dist from k to all nodes to infinity
dist[k] = 0                       # starting node (k) dist is 0

heap = [(0, k)]                   # start path from node k.
while heap:                       # use min-heap to auto-sort by nodes by shortest weights
    dist, node = heapq.heappop(heap)

    if dist > dist[node]:         # skip stale entries
        continue

    for neighbor, weight in graph[node]:
        new_dist = dist + weight

        if new_dist < dist[neighbor]:   # relax outgoing edges
            dist[neighbor] = new_dist
            heapq.heappush(heap, (new_dist, neighbor))

Dijkstra vs. your previous BFS algorithms

Algorithm	        What determines processing order?	            Typical purpose
Ordinary BFS	    FIFO queue	                                    Shortest paths in unweighted graphs
Multi-source BFS	FIFO queue initialized with multiple sources	Minimum propagation steps
Kahn's BFS	        Queue of nodes with indegree zero	            Topological ordering
Dijkstra	        Min-heap ordered by total distance	            Shortest paths in nonnegative weighted graphs

Ordinary BFS is basically a special case of Dijkstra, when every edge has same positive weight.
In that case, processing nodes by BFS level is equivalent to processing them by increasing shortest distance.
