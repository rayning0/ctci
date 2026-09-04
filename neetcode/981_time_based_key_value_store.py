# https://leetcode.com/problems/time-based-key-value-store/description/
# https://neetcode.io/solutions/time-based-key-value-store
# Binary Search: Versioned Data
# UPPER BOUND on timestamp

# set(): Stores a key, value, and timestamp. Timestamps for any key arrive in strictly increasing order.
# get(): Finds value linked to largest timestamp <= target timestamp. If no matching timestamp exists, returns "".

# Ex: timestamps = [1, 4, 6, 8, 10]
# target = 7. We want timestamp 6.
# upper_bound(7) = first timestamp > 7 = index 3
# timestamps: [1, 4, 6, | 8, 10]
# desired timestamp 6 is 1 before this boundary.
# index = upper_bound(target) - 1

# "All timestamps of set() are strictly increasing." <--- KEY! We don't need to sort input by timestamp!

# 1. Binary search on list. BEST ANSWER for interview!

class TimeMap:
    """Store values linked to keys and timestamps.
    Each key maps to timestamped values. set() stores a new value at a certain timestamp,
    while get() retrieves the value linked to latest timestamp <= requested timestamp.
    """

    def __init__(self):
        # {key1: [list of (timestamp, value) where timestamp always goes up], key2: [list of (ts, val)]}
        # {'foo': [(1, 'bar'), (4, 'bar2')], 'alice': [(1, 'happy'), (3, 'sad')]}
        self.map = {}

    # Time: O(1) amortized, Space: O(1) per call, O(N) total for all entries
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        self.map[key].append((timestamp, value))

    # Since all timestamps already sorted, use binary search on timestamps!
    # Seek UPPER BOUND on timestamp.
    # See https://github.com/rayning0/ctci/blob/master/neetcode/034_find_first_and_last_position_of_element_in_sorted_array.py
    # Time: O(log n), Space: O(1) auxiliary
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''

        entries = self.map[key]

        # UPPER BOUND(target) =  First index for timestamp > target = l
        # Desired value (largest timestamp <= target) is one index before it.
        # So last = l - 1
        l, r = 0, len(entries)
        while l < r:
            mid = (l + r) // 2
            ts, value = entries[mid]

            if ts > timestamp:
                r = mid
            else:
                l = mid + 1

        # If all timestamps > target timestamp.
        # Ex: entries = [(5, "a"), (7, "b")]. get("foo", 3)
        if l == 0:
            return ''

        ts, value = entries[l - 1]   # subtract 1 from i to get actual element

        return value

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    obj = TimeMap()

    obj.set("foo", "bar", 1)
    assert obj.get("foo", 1) == "bar"
    assert obj.get("foo", 3) == "bar"  # no value links to foo at timestamp 3 or 2, so only value is at timestamp 1 (or "bar")

    obj.set("foo", "bar2", 4)
    assert obj.get("foo", 4) == "bar2"
    assert obj.get("foo", 5) == "bar2"
    assert obj.get("foo", 0) == ""
    assert obj.get("foo", 1) == "bar"

    obj.set("alice", "happy", 1)
    assert obj.get("alice", 1) == "happy"
    assert obj.get("alice", 2) == "happy" # no value stored for timestamp 2, so return value at timestamp 1

    obj.set("alice", "sad", 3)
    assert obj.get("alice", 3) == "sad"
    assert obj.get("alice", 2) == "happy"
    assert obj.get("alice", 1) == "happy"
    print("All tests passed!")

# 2. Use max heap and sorted(). Not optimal. For case where each new set() has timestamp in RANDOM ORDER.
# Make hashmap with key and value = maxheap = [(-timestamp1, value1), (-timestamp2, value2), ...]

import heapq

class TimeMap:

    def __init__(self):
        self.map = {}

    # Time: O(log n), Space: O(n)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []                              # make new heap for each new key

        heapq.heappush(self.map[key], (-timestamp, value))  # max heap

        # OR
        # heap = self.map.setdefault(key, [])
        # heapq.heappush(heap, (-timestamp, value))

    # Time: O(n log n), Space: O(n)
    def get(self, key: str, timestamp: int) -> str:
        heap = self.map[key]
        # print(f"\nkey: {key}, heap: {sorted(heap)}, timestamp: {timestamp}")

        for ts, value in sorted(heap):  # Must resort heap each loop! sorted() has O(n log n) time
            # print(f"Check ({ts}, {value}). Is {-ts} <= {timestamp}? {-ts <= timestamp}")
            if -ts <= timestamp:
                # print(f"Value: {value}")
                return value

        # print("Value: ''")
        return ''
___________________________
obj.map = {'foo': [(-4, 'bar2'), (-1, 'bar')], 'alice': [(-3, 'sad'), (-1, 'happy')]}

key: foo, heap: [(-1, 'bar')], timestamp: 1
Check (-1, bar). Is 1 <= 1? True
Value: bar

key: foo, heap: [(-1, 'bar')], timestamp: 3
Check (-1, bar). Is 1 <= 3? True
Value: bar

key: foo, heap: [(-4, 'bar2'), (-1, 'bar')], timestamp: 4
Check (-4, bar2). Is 4 <= 4? True
Value: bar2

key: foo, heap: [(-4, 'bar2'), (-1, 'bar')], timestamp: 5
Check (-4, bar2). Is 4 <= 5? True
Value: bar2

key: foo, heap: [(-4, 'bar2'), (-1, 'bar')], timestamp: 0
Check (-4, bar2). Is 4 <= 0? False
Check (-1, bar). Is 1 <= 0? False
Value: ''

key: foo, heap: [(-4, 'bar2'), (-1, 'bar')], timestamp: 1
Check (-4, bar2). Is 4 <= 1? False
Check (-1, bar). Is 1 <= 1? True
Value: bar

key: alice, heap: [(-1, 'happy')], timestamp: 1
Check (-1, happy). Is 1 <= 1? True
Value: happy

key: alice, heap: [(-1, 'happy')], timestamp: 2
Check (-1, happy). Is 1 <= 2? True
Value: happy

key: alice, heap: [(-3, 'sad'), (-1, 'happy')], timestamp: 3
Check (-3, sad). Is 3 <= 3? True
Value: sad

key: alice, heap: [(-3, 'sad'), (-1, 'happy')], timestamp: 2
Check (-3, sad). Is 3 <= 2? False
Check (-1, happy). Is 1 <= 2? True
Value: happy

key: alice, heap: [(-3, 'sad'), (-1, 'happy')], timestamp: 1
Check (-3, sad). Is 3 <= 1? False
Check (-1, happy). Is 1 <= 1? True
Value: happy
All tests passed!

# 3. Use bisect library. Best answer if each new set() has timestamps in RANDOM ORDER.

from bisect import bisect_right, insort

class TimeMap:
    def __init__(self):
        self.map = {}

    # Time: O(n). Binary search is O(log n), but list insertion shifts up to n elements
    # Space: O(n)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []

        # bisect.insort() inserts element into list, keeping its sorted order.
        # It saves you from appending item, then sorting whole list again.
        # bisect.insort() = bisect.insort_right() finds correct position by binary search, then inserts
        # (to right of existing identical elements) while keeping list sorted
        insort(self.map[key], (timestamp, value))

    # Time: O(log n). bisect_right is pure binary search
    # Space: O(1)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        entries = self.map[key]

        # bisect.bisect_right() = bisect.bisect() function finds insertion index for element in sorted list to maintain sorted order.
        # If element already exists, it returns index to RIGHT of last occurrence.
        i = bisect_right(entries, (timestamp, chr(127)))
        if i == 0:
            return ""

        ts, value = entries[i - 1]  # subtract 1 from i to get actual element

        return value
___________________________
get() must find rightmost entry whose timestamp ≤ the target timestamp.

Ex: Suppose we called set() 4 times for key "foo". Now let's call get("foo", 4).
entries = [(1, "a"), (3, "b"), (5, "c"), (7, "d")]

1. bisect_right() finds "where would I insert (4, infinity)?"
entries:  (1,"a")  (3,"b")  (5,"c")  (7,"d")
                          ↑
                   insert at index = 2

bisect_right returns i = 2, index after everything ≤ (4, chr(127)).

2. Subtract 1 index value.
i - 1 = 1 → entries[1] = (3, "b") → return "b"
Timestamp 3 is largest timestamp ≤ 4.

3. Why use chr(127)?
It handles the exact match case. Try get("foo", 5):

Search target: (5, chr(127))    ← chr(127) is highest possible value
entries:  (1,"a")  (3,"b")  (5,"c")  (7,"d")
                                    ↑
                              insert here → i = 3
Since "c" < chr(127), (5, "c") < (5, chr(127)), so bisect_right lands after it at index 3.
Step back: i - 1 = 2 → entries[2] = (5, "c") → return "c"
Without chr(127), searching for just (5,) could land before (5, "c"), missing the exact match.

ASCII defines 128 characters, 0-127:

Range	Examples
0–31	Control characters (newline, tab, etc.)
32–126	Printable characters (letters, digits, symbols)
127	    DEL — the last/highest ASCII code

chr(127) is guaranteed upper bound for the string tiebreaker, ensuring bisect_right always lands AFTER any real value at the same timestamp.

_________________
Algorithmic Decision Challenge

You are building a distributed configuration versioning service. Each service instance pushes configuration updates by appending new versions with monotonically increasing timestamps — historical versions are never modified or deleted, only new ones are added. Other services query the configuration state at a specific point in time to retrieve the most recent version that was active at that moment.

System characteristics:

- 100 million total operations per day, with a 95% read / 5% write ratio.
- Configuration versions are always appended in non-decreasing timestamp order per key.
- Average 1,000 historical versions per key, with some high-traffic keys reaching 100,000 versions.
- Read latency p99 must stay under 10μs.
- The service must correctly return the configuration value associated with the largest timestamp ≤ the queried timestamp.

Which data structure and query strategy would you recommend?

[Options]

A. Hash map mapping each key to an append-only list of (timestamp, value) pairs; use lower-bound binary search on the timestamp array for reads

B. Hash map mapping each key to a list of (timestamp, value) pairs; use linear backward scan from the most recent entry for reads

C. Hash map mapping each key to a balanced binary search tree (e.g., red-black tree) keyed by timestamp; use tree search for reads

D. Hash map mapping each key to only the latest (timestamp, value) pair; return it if its timestamp ≤ the queried timestamp, otherwise return empty

[Option Analysis]

Option A (Correct): Append-only list is O(1) per write. Binary search is O(log n) per read — for 100K versions, that's ~17 comparisons on a contiguous array, well within 10μs. The sorted-timestamp guarantee means no sorting overhead is needed. Simple to implement and debug.

Option B (Suboptimal): Linear backward scan is O(n) per read. With 1,000 versions on average (and up to 100K), this regularly exceeds the 10μs p99 budget. The 95% read ratio means this penalty is paid on the vast majority of operations.

Option C (Contextually suboptimal): Also O(log n) reads, but a balanced BST introduces pointer chasing (cache-unfriendly), per-node memory allocation overhead, and significantly more complex implementation (rotations, rebalancing). Since timestamps are already sorted on insertion, the BST's ability to handle arbitrary insertion order provides no benefit — you'd be paying engineering and runtime cost for a capability you never use.

Option D (Incorrect): Stores only latest version. The requirement is to return the value with the largest timestamp ≤ queried timestamp. If queried timestamp is older than latest version, Option D returns empty, losing all historical data. Fundamentally incompatible with the versioning requirement.

[What-If Challenge]

Suppose the constraint "timestamps are always appended in non-decreasing order" is removed — versions could arrive out of order due to network delays or clock skew. Would your choice change, and why?

The max heap + sorted() solution has issues worth unpacking:

- A max heap gives you the maximum timestamp efficiently, but this problem asks for the largest timestamp ≤ target — not the global maximum. A heap can't answer that query without extracting elements one by one, which is O(n) in the worst case.
- Using sorted() to re-sort on each read is O(n log n) per query — far worse than the 10μs budget.
- Even inserting into a sorted list to maintain order is O(n) per write (shifting elements).

Why the balanced BST wins here:

Operation	                Balanced BST
Insert (unsorted)	        O(log n) — tree handles ordering automatically
Query (floor/predecessor)	O(log n) — standard tree search

The BST's floor query directly solves "largest timestamp ≤ target" even with arbitrary insertion order — at the cost of higher constant factors (pointer chasing, node allocation) compared to Option A's array-based binary search.

The sorted-timestamp guarantee is what makes Option A's simple array approach viable. Without it, you pay for a more complex data structure (BST) to maintain order dynamically. This is a classic engineering trade-off: simpler data structure + data guarantees vs. more complex data structure + no guarantees.
