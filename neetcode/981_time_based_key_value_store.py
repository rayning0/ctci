# https://leetcode.com/problems/time-based-key-value-store/description/
# https://neetcode.io/solutions/time-based-key-value-store
# Binary Search: Versioned Data
# UPPER BOUND on timestamp

# set(): Stores a key, value, and timestamp. Timestamps for any key arrive in strictly increasing order.
# get(): Finds value linked to largest timestamp <= target timestamp. If no matching timestamp exists, returns "".

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

        # UPPER BOUND(target) =  First index whose value > target = LOWER BOUND(target + 1) = l
        # But since we want last position of target, last = l - 1
        l, r = 0, len(entries)
        while l < r:
            mid = (l + r) // 2
            ts, value = entries[mid]

            if ts <= timestamp: # or "ts < timestamp + 1"
                l = mid + 1
            else:               # ts > timestamp
                r = mid

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
