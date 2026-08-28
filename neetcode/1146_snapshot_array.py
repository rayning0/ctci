# https://leetcode.com/problems/snapshot-array/description/
# https://algo.monster/liteproblems/1146
# Binary Search: Versioned Data

class SnapshotArray:
    """1. SnapshotArray(length) initializes array-like data structure with length. Each element = 0.
    2. set(index, val) sets element at index equal to val.
    3. snap() takes a snapshot of array and returns snap_id: total # of times we called snap() - 1.
    4. get(index, snap_id) returns value at index, at time we took snapshot with snap_id
    """
# self.list = [[5, 0, 0], [6, 0, 0]] <--- index of self.list is snap_id
# self.list = [[0, 5, 0], [0, 7, 9]]

    def __init__(self, length: int):
        self.list = [[0] * length]
        self.snap_id = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        print(f"in set(): snap_id: #{self.snap_id}, index: {index}")
        self.list[self.snap_id][index] = val
        print(self.list)

    def snap(self) -> int:
        self.snap_id += 1
        self.list.append([0] * self.length)   # add new [0, 0, 0, ...] to end of list

        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.list[snap_id][index]

    def print(self) -> list[list[int]]:
        return self.list

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index, val)
# param_2 = obj.snap()
# param_3 = obj.get(index, snap_id)

if __name__ == "__main__":
    obj = SnapshotArray(3)      # [[0, 0, 0]]
    obj.set(0, 5)               # [[5, 0, 0]]
    assert obj.snap() == 0      # Stores state [5, 0, 0]. snap_id = 0
    obj.set(0, 6)               # [[5, 0, 0], [6, 0, 0]]
    assert obj.get(0, 0) == 5   # Get snap_id 0 [5, 0, 0], index 0. Gets 5.

    # Overwriting values and multiple snaps
    obj = SnapshotArray(3)      # [[0, 0, 0]]
    obj.set(1, 5)               # [[0, 5, 0]]
    assert obj.snap() == 0      # Stores state [0, 5, 0]. snap_id = 0
    obj.set(1, 7)               # [[0, 5, 0], [0, 7, 0]]
    obj.set(2, 9)               # [[0, 5, 0], [0, 7, 9]]
    assert obj.snap() == 1      # Stores state [0, 7, 9]. snap_id = 1
    assert obj.get(1, 0) == 5   # Get snap_id 0 [0, 5, 0], index 1. Gets 5.
    assert obj.get(1, 1) == 7   # Get snap_id 1 [0, 7, 9], index 1. Gets 7.

    print("All tests passed!")
