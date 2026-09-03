# https://leetcode.com/problems/car-pooling/description/
# https://neetcode.io/solutions/car-pooling
# Intervals: Sweep Line with Difference Array

# See https://github.com/rayning0/ctci/blob/master/neetcode/253_meeting_rooms_ii.py,
# especially its min heap solution.

# 1. Sweep Line with Difference Array (Bucket technique). BEST for interview!

# Since trip locations are bounded within [0, 1000],
# we can use an array of size 1001 to record passenger changes at each location,
# then compute a prefix sum to get running count.
# This eliminates sorting entirely, improving Big O time.

# Time: O(n + L), Space: O(L) where L = max location (1000), n = len(trips)
def carPooling(trips: list[list[int]], capacity: int) -> bool:
    # Difference array: +people at pickup, -people at dropoff
    diff = [0] * 1001   # Problem says: "1 <= trips.length <= 1000". Trip #'s start from 1.
    count = 0

    for people, start, end in trips:
        diff[start] += people
        diff[end] -= people

    for people in diff:
        count += people
        if count > capacity:
            return False

    return True


# 2. Sweep Line with sorted event list
# Time: O(n log n), Space: O(n)
def carPooling(trips: list[list[int]], capacity: int) -> bool:
    events = []
    count = 0       # current # of people in car

    for people, start, end in trips:
        events.append((start, people))  # (pick up location,  # of people to add)
        events.append((end, -people))   # (drop off location, # of people to subtract)

    events.sort()
    # sorts events list in ascending order by:
    # 1. location, then by
    # 2. people
    # events.sort(key=lambda event: (event[0], event[1]))

    # Python's tuple comparison is already lexicographic:
    # events.sort() and events.sort(key=lambda e: (e[0], e[1])) produce exact same order. The explicit key is unneeded.

    for _, people in events:
        count += people
        if count > capacity:
            return False

    return True


if __name__ == "__main__":
    assert carPooling([[2,1,5],[3,3,7]], 4) == False
    assert carPooling([[2,1,5],[3,3,7]], 5) == True
    assert carPooling([[4,1,2],[3,2,4]], 4) == True
    assert carPooling([[2,1,3],[3,2,4]], 4) == False
    assert carPooling([[7,5,6],[6,7,8],[10,1,6]], 16) == False
    assert carPooling([[3,5,9],[4,2,5],[3,4,6],[9,1,4],[5,6,8],[5,4,6]], 14) == True
    print("All tests passed!")


# 0  1    2   3   4   5   6   7   8   9
#                     3---------------3
#         4-----------4
#                 3-------3
#     9-----------9
#                         5-------5
#                 5-------5
                                          # event:
# At 1, pick up 9 people = 9 in car         (1,  9)
# At 2, pick up 4 people = 13               (2,  4)
# At 4, drop off 9 people = 4               (4, -9)
# At 4, pick up 3 + 5 people = 12           (4,  3), (4, 5)
# At 5, drop off 4 people = 8               (5, -4)
# At 5, pick up 3 people = 11               (5,  3)
# At 6, drop off 3 + 5 people = 3           (6, -3), (6, -5)
# At 6, pick up 5 people = 8                (6,  5)
# At 8, drop off 5 people = 3               (8, -5)
# ____________________________
# For whole trip, we never exceed max capacity of 14.

# events =

# before sort
# [(5, 3), (9, -3), (2, 4), (5, -4), (4, 3), (6, -3), (1, 9), (4, -9), (6, 5), (8, -5), (4, 5), (6, -5)]
# after sort
# [(1, 9), (2, 4), (4, -9), (4, 3), (4, 5), (5, -4), (5, 3), (6, -5), (6, -3), (6, 5), (8, -5), (9, -3)]
___________________________
Algorithm Decision Challenge

You are building a compliance monitoring module for a city rideshare platform. The system must verify that no shuttle exceeds its passenger capacity at any point during the day, based on logged trip records.

The platform operates under these conditions:

- Approximately 2 million trips are logged per day across the city.
- All pickups and dropoffs occur within 500 designated zones (zone IDs range from 0 to 499).
- The compliance check runs as a real-time API endpoint that must respond within 50ms per query.
- The service runs inside a container with a strict 256MB memory limit.

You need to implement the core check: given a batch of trips and a capacity threshold, determine whether any shuttle ever exceeds capacity.

Which approach would you choose?

[Options]

A. Event-based sweep line: create (location, ±passengers) events for all trips, sort the 4 million events by location, then sweep through to track running passenger count.

B. Difference array: allocate a fixed-size array of 500 elements, record +passengers at each pickup zone and -passengers at each dropoff zone, then compute a single prefix sum pass to check capacity.

C. Hash map difference table: use a dictionary to accumulate +passengers and -passengers per zone, sort the dictionary keys, then iterate in order to compute running passenger count.

[Option Analysis]

A (Event sweep line): Suboptimal here. Sorting 4M event tuples is both time-expensive (O(n log n)) and memory-heavy in Python (each tuple is a heap object). Reasonable when L is unbounded or n is small — not this scenario.

Option A would use O(2 million) space for its events list, far over 256 MB memory limit. Plus its sort of events makes it much slower, at O(2 million * log(base 2) 2 million) = O(2 million * 21) = O(41 million).

B (Difference array): Best fit. O(n + L) time with a single pass to build the array and a 500-element prefix sum. Fixed, predictable memory. Cache-friendly sequential access. Meets both the latency and memory constraints comfortably.

Option B is best, with fixed size array of only 500. Then it uses O(2 million + 500) time, O(500) space, definitely below 256 MB memory limit.

C (Hash map difference table): Adds hash table overhead per insertion with no space benefit (500 zones fit trivially in an array). Sorting keys reintroduces O(L log L), which is negligible here but still unnecessary overhead. Best suited for sparse, large-range locations.

Option C with a dict is only good if L (locations) >> n (trips). But here, n is huge (2 million) while locations is small (500). It has same Big O values as option A.

[What-If Challenge]

Q: Suppose the platform expands to a national network where trips span 100,000 possible GPS coordinate buckets instead of 500 zones, but daily trips remain at 2 million. Would your choice change? Why or why not?

No, because O(n + L) for option B is still faster than that for Options A and C.
n = 2 million, L = 100K. For space, O(L) for option B < O(n) for options A and C.

Option B remains the best choice. O(n + L) = O(2.1M) still beats O(n log n), and O(L) space still beats O(n). The answer doesn't change.

How to estimate if 100K elements fit in 256MB:

Calculate per-element cost in Python:

Python list of ints:
  - List of pointers:  100,000 × 8 bytes  = 800 KB
  - Int objects (small ints are cached):    ~0 extra
  - Int objects (large/unique):  100,000 × 28 bytes = 2.8 MB
  ─────────────────────────────────────────────────
  Total: ~3.6 MB
3.6 MB << 256 MB — nowhere close to the limit.

What Option A would cost:

4M event tuples:
  - List of pointers:   4,000,000 × 8 bytes  = 32 MB
  - Tuple objects:      4,000,000 × 56 bytes = 224 MB
  - Int objects inside: 8,000,000 × 28 bytes = 224 MB
  ──────────────────────────────────────────────────
  Total: ~480 MB  ❌ Exceeds 256 MB
Rule of thumb for Python memory estimation:

Structure	        Per-element cost
int in list	        ~8 bytes (pointer) + 28 bytes (object) ≈ 36 bytes
tuple(int, int)	    ~56 bytes (tuple) + 56 bytes (2 ints) ≈ 112 bytes
dict entry	        ~72 bytes (hash + key ptr + value ptr) + key/value objects

So even at L = 100K, the difference array uses ~130× less memory than the event list. The choice stays the same — just verify the math when L grows large enough that O(L) starts becoming non-trivial.
