# https://leetcode.com/problems/snapshot-array/description/
# https://algo.monster/liteproblems/1146
# Binary Search: Versioned Data
# UPPER BOUND on snap_id

# Option B: Per-index version history with binary search
# For each index, keep list of (snap_id, value) tuples, recording only when that index changed.
# In get(), use binary search on snap_id.

class SnapshotArray:
    """1. SnapshotArray(length) initializes array-like data structure with length. Each element = 0.
    2. set(index, val) sets element at index equal to val.
    3. snap() takes a snapshot of array and returns snap_id: total # of times we called snap() - 1.
    4. get(index, snap_id) returns value at index, at time we took snapshot with snap_id
    """

    # Time: O(n), Space: O(n)
    def __init__(self, length: int):
        self.history = [[] for _ in range(length)]   # makes [[], [], [], ...]
        self.snap_id = 0

    # Time: O(1) amortized, Space: O(1) auxiliary
    def set(self, index: int, val: int) -> None:
        history = self.history[index]

        # OPTIONAL to save memory:
        # if see multiple updates to same index before snap(), only use last one
        # if history and history[-1][0] == self.snap_id:
        #     history[-1] = (self.snap_id, val)
        # else:
        history.append((self.snap_id, val))

    # Time: O(1), Space: O(1)
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    # Time: O(log k), Space: O(1) auxiliary
    # k = len(self.history[index]), # of recorded updates for index.
    # UPPER BOUND on snap_ids
    def get(self, index: int, snap_id: int) -> int:
        history = self.history[index]

        l, r = 0, len(history)
        while l < r:
            mid = (l + r) // 2
            id, val = history[mid]

            if id <= snap_id:
                l = mid + 1
            else:
                r = mid

        # If all entries are > target snap_id
        # Ex: history[3] = [(3, 42)]. get(3, 2). No entry has snap_id <= 2.
        if l == 0:
            return 0

        id, val = history[l - 1]    # subtract 1 from l to get actual element

        return val

> SnapshotArray(4)

snap_id = 0
history = [
    [],    # index 0
    [],    # index 1
    [],    # index 2
    [],    # index 3
]

> set(0, 5)
> set(0, 10)
> set(2, 7)

history = [
    [(0, 5), (0, 10)],    # index 0
    [],                   # index 1
    [(0, 7)],             # index 2: changed at snap 0
    [],                   # index 3
]

> snap()        # returns 0. snap_id = 1
> set(1, 99)
> set(0, 3)

snap_id = 1
history = [
    [(0, 5), (0, 10), (1, 3)],   # index 0: three entries
    [(1, 99)],
    [(0, 7)],
    [],
]

> snap()        # returns 1. snap_id = 2
> snap()        # returns 2. snap_id = 3
> set(3, 42)

snap_id = 3
history = [
    [(0, 5), (0, 10), (1, 3)],   # index 0
    [(1, 99)],                   # index 1
    [(0, 7)],                    # index 2
    [(3, 42)],                   # index 3: first change at snap 3
]

> snap()        # returns 3.
snap_id = 4

> get(0, 2): index 0 at snap_id 2

in history[0] = [(0, 5), (0, 10), (1, 3)],
binary search for right-most entry with snap_id <= 2
snap_ids: [0, 0, 1] all <= 2. Rightmost entry = (1, 3). Value = 3.

> get(0, 0): index 0 at snap_id 0

in history[0] = [(0, 5), (0, 10), (1, 3)],
binary search for right-most entry with snap_id <= 0
snap_ids:  [0, 0, 1]
               ^ <--- position 1. So entry = (0, 10). Value = 10

> get(3, 2): index 3 at snap_id 2
in history[3] = [(3, 42)],
binary search for right-most entry with snap_id <= 2
snap_ids: [3]
           >2  <--- No valid entry! Return 0 (default)

> get(3, 3): index 3 at snap_id 3
in history[3] = [(3, 42)],
                    ^ <--- rightmost. Value = 42

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index, val)
# param_2 = obj.snap()
# param_3 = obj.get(index, snap_id)

if __name__ == "__main__":
    obj = SnapshotArray(3)      # [[],               [], []] = history
    obj.set(0, 5)               # [[(0, 5)],         [], []]
    assert obj.snap() == 0      # snap_id = 1
    obj.set(0, 6)               # [[(0, 5), (1, 6)], [], []]
    assert obj.get(0, 0) == 5   #      ^

    # Overwriting values and multiple snaps
    obj = SnapshotArray(3)      # [[],       [],                []] = history
    obj.set(1, 5)               # [[],       [(0, 5)],          []]
    assert obj.snap() == 0      # snap_id = 1
    obj.set(1, 7)               # [[],       [(0, 5), (1, 7)],  []]
    obj.set(2, 9)               # [[],       [(0, 5), (1, 7)],  [(1, 9)]]
    assert obj.snap() == 1      # snap_id = 2
    assert obj.get(1, 0) == 5   # From [(0, 5), (1, 7)], get (0, 5). Value = 5
    assert obj.get(1, 1) == 7   # From [(0, 5), (1, 7)], get (1, 7). Value = 7

    # Consecutive Snaps Without Changes
    obj = SnapshotArray(2)      # [[],              []] = history
    obj.set(0, 99)              # [[(0, 99)],       []]
    assert obj.snap() == 0      # snap_id = 1
    assert obj.snap() == 1      # snap_id = 2
    assert obj.snap() == 2      # snap_id = 3
    assert obj.get(0, 0) == 99  # From [(0, 99)], get (0, 99). Value = 99
    assert obj.get(0, 1) == 99  # From [(0, 99)], get (0, 99). Value = 99
    assert obj.get(0, 2) == 99  # From [(0, 99)], get (0, 99). Value = 99

    # LeetCode AI example
    obj = SnapshotArray(4)
    obj.set(0, 5)
    obj.set(0, 10)
    obj.set(2, 7)
    assert obj.history ==   [
                                [(0, 5), (0, 10)],    # index 0
                                [],                   # index 1
                                [(0, 7)],             # index 2: changed at snap 0
                                []                    # index 3
                            ]
    assert obj.snap() == 0      # returns 0. snap_id = 1
    obj.set(1, 99)
    obj.set(0, 3)
    assert obj.snap() == 1
    assert obj.snap() == 2
    obj.set(3, 42)
    assert obj.snap() == 3      # returns 3. snap_id = 4
    assert obj.history ==   [
                                [(0, 5), (0, 10), (1, 3)],   # index 0
                                [(1, 99)],                   # index 1
                                [(0, 7)],                    # index 2
                                [(3, 42)]                    # index 3: first change at snap 3
                            ]
    assert obj.get(0, 2) == 3
    assert obj.get(0, 0) == 10
    assert obj.get(3, 2) == 0
    assert obj.get(3, 3) == 42
    print("All tests passed!")

# Option A: Full array copy per snapshot

    def __init__(self, length: int):
        self.list = [[0] * length]
        self.snap_id = 0

    # Time: O(1)
    def set(self, index: int, val: int) -> None:
        print(f"in set(). snap_id: {self.snap_id}, index: {index}, val: {val}")
        self.list[self.snap_id][index] = val
        print(self.list)

    # Time: O(n). Space: O(n * s)
    def snap(self) -> int:
        copy = list(self.list[-1])
        self.list.append(copy)    # append copy of latest version of list to end of list
        self.snap_id += 1

        return self.snap_id - 1

    # Time: O(1)
    def get(self, index: int, snap_id: int) -> int:
        print(f"in get(). snap_id: {snap_id}, index: {index}")
        print(self.list)
        return self.list[snap_id][index]

    def print(self) -> list[list[int]]:
        return self.list
# _____________________
Algorithm Decision Challenge:

You are building a versioned key-value configuration store for a distributed system. The system manages a configuration array of 200,000 integer entries.

> Operational characteristics:

- Configuration changes are sparse: each update batch modifies only 5–20 entries out of 200,000.
- The system takes a snapshot after every update batch for audit and rollback. Over the system's lifetime, 5,000+ snapshots accumulate.
- get() is called thousands of times per second by monitoring dashboards and rollback services. Each query must return in well under 1 ms.
- The service runs on a container with a 256 MB memory limit.
- Your team is evaluating how to implement the snapshot mechanism. Which approach would you recommend?

[Options]

A. Full array copy per snapshot — on each snapshot, copy entire current array as the new snapshot state.

B. Per-index version history with binary search — for each index, maintain list of (snap_id, value) entries recording only when that index changed. Use binary search on get().

C. Centralized change log with linear scan — store all (snap_id, index, value) changes in single global list sorted by snap_id. On get(), scan backward from the queried snap_id to find the latest value for the given index.

[Option Analysis]

Option A (Full copy): 200K entries × 5,000 snapshots = ~36 GB. Immediately eliminated by the 256 MB memory limit. Simple to implement, but physically infeasible.

1 Python list of 200,000 ints:
  - 200,000 pointers (8 bytes each)    = 1.6 MB
  - 200,000 int objects (~28 bytes each) = 5.6 MB
  - Total per array                     ≈ 7.2 MB

5,000 snapshots = 5,000 × 7.2 MB ≈ 36 GB

n = 200,000    s = 5,000

Each snapshot stores a full array of n elements.

snap() total cost:  O(n × s) = 200,000 × 5,000 = 10⁹ operations
Total memory:       O(n × s) = ~4 GB (compact) to ~36 GB (Python)
The strength of Option A is its O(1) get — it's the fastest possible query. But the cost is paid upfront at every snap(): copying 200,000 elements each time, and storing all of them forever.

Trade-off: Option A buys the fastest reads (O(1)) at the expense of the most expensive snapshots (O(n)) and the largest memory footprint (O(n×s)) — which is exactly what the sparse-update scenario makes wasteful.

Option B (Per-index history + binary search): Memory = only (snap_id, val) pairs for actual changes. With sparse updates (~10 changes per snapshot × 5,000 snapshots = ~50K tuples), memory is negligible. get() is O(log s) where s = changes to that index — often single digits. Easily sub-millisecond.

> Why is Option B's get() < 1 ms?

Binary search cost depends on the size of the list being searched — which is the number of times that specific index was changed, not total changes.

With sparse updates (~10 changes per snapshot across 200,000 indices):

Expected changes per index over 5,000 snapshots:
  ≈ (10 changes/snapshot × 5,000 snapshots) / 200,000 indices
  ≈ 0.25 changes per index
Most indices have 0 or 1 entry. Even a heavily modified index might have 100–200 entries.

bisect on 1 entry:    1 comparison
bisect on 200 entries: 8 comparisons
bisect on 5,000 entries (worst case — index changed every snapshot): 13 comparisons
Each comparison is a simple integer check. ~13 comparisons takes well under 1 microsecond — far below 1 ms.

Option C (Centralized log + linear scan): Same memory as B, but get() is O(total_changes) — potentially scanning 50K+ entries per query. At thousands of queries per second, this becomes a CPU bottleneck and risks exceeding the sub-millisecond target.

> Why can't Option C use binary search?

Binary search requires the list to be searchable by a single sorted key. Option C's log is sorted by snap_id, but get() needs to filter by 2 conditions simultaneously: snap_id ≤ target AND index == target.

changes = [
    (0, 0, 5),     # snap 0, index 0
    (0, 3, 12),    # snap 0, index 3
    (1, 1, 10),    # snap 1, index 1
    (1, 0, 8),     # snap 1, index 0  ← we want this
    (2, 3, 20),    # snap 2, index 3
]
Query: get(index=0, snap_id=2)

If you binary search on snap_id, you find the boundary at position 4 (snap 2). But entries for index 0 are scattered at positions 0 and 3 — there's no way to jump to them without scanning.

By snap_id:   sorted ✅    → binary search works for snap_id alone
By index:     NOT sorted ❌ → entries for index 0 are at [0, 3, ...] — scattered
To make binary search work for both conditions, you'd need to restructure the data — which brings you right back to Option B (per-index history, where each index's list is naturally sorted by snap_id).
__________________________
What-If Challenge:

"What if updates were dense instead of sparse — say, each snapshot modifies 80% of the 200,000 entries? Would Option B still be preferable, or would the trade-off shift? Why?"

- Dense update math

80% of 200,000 = 160,000 changes per snapshot
Over 5,000 snapshots: 160,000 × 5,000 = 800 million total entries

- Option B under dense updates

Each index's history now has ~4,000 entries (no longer 0–1):

Memory: 200,000 indices × 4,000 entries × ~8 bytes ≈ 6.4 GB (compact)
        In Python: ~64 GB
get():  binary search on 4,000 entries ≈ 12 comparisons (still fast)

- Option C under dense updates

Memory: same ~6.4 GB (same total entries, just in one list)
get():  linear scan through up to 800 million entries. Several seconds per query

What actually changes

            Sparse (original)	Dense (80%)
B memory	~few MB	            ~6.4 GB ❌
C memory	~few MB	            ~6.4 GB ❌
A memory	~4 GB	            ~4 GB (unchanged!)

Notice something surprising? Option A's memory doesn't change with update density — it's always O(n × s). But Options B and C explode when updates become dense, because they store per-change rather than per-snapshot.

> The correct answer:

Under dense updates, none of the 3 options work well within 256 MB. But the trade-off fundamentally shifts:

- B loses its core advantage (small per-index histories) — memory approaches Option A's, but with slower O(log s) reads instead of O(1).
- Option A becomes relatively more attractive: same memory as B, but with O(1) get and O(n) snap — and O(n) snap is already happening anyway since 80% of the array is being written between snapshots.
- Option C is still the worst due to linear scan on a massive log.

Key insight: the sparsity of updates is what makes Option B powerful. Remove sparsity, and you lose the only reason to prefer it over Option A.

For truly dense updates at this scale, you'd need a different strategy entirely — such as only storing snapshots at intervals and recomputing intermediate states, or accepting that 256 MB simply can't hold this much history.
