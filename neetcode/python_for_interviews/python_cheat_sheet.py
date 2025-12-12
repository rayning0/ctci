# Python Cheat Sheet: quick Python review
# https://neetcode.io/courses/lessons/python-for-coding-interviews
# Even better: https://static.realpython.com/python-cheatsheet.pdf

# VARIABLES

# are dynamically typed
n = 0
print("n =", n)
# >>> n = 0

n = "abc"
print("n =", n)

# String interpolation
name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}')

a = 12
b = 3
print(f'12 multiply 3 is {a * b}.')


# >>> n = abc

# Multiple assignments
n, m = 0, "abc"
n, m, z = 0.125, "abc", False

# None is null (absence of value)
n = 4
n = None
print("n =", n)
# >>> n = None

# IF-STATEMENTS

# Don't need parentheses
# or curly braces.
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multi-line conditions.
# and = &&
# or  = ||
n, m = 1, 2
if (n > 2 and n != m) or n == m:
    n += 1

# LOOPS

n = 5
while n < 5:
    print(n)
    n += 1

# Looping from i = 0 to i = 4
for i in range(5):
    print(i)

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

# MATH

# Division is decimal by default
print(5/2)
2.5

# Double slash rounds down
print(5 // 2)
2

# Most languages round towards 0 by default. Here, negative numbers round down.
print(-3 // 2)
-2

# A workaround for rounding towards 0: Use decimal division, then convert to int
print(int(-3/2))
-1

10 % 3 = 1
-10 % 3 = 2 # negative values for mod are a surprise

# To match other languages:
import math

math.fmod(-10, 3) = -1
math.floor(3 / 2) = 1
math.ceil(3 / 2) = 2
math.floor(-3 / 2) = -2
math.sqrt(2)
math.pow(2, 3) = 8.0 #  <---- always gives float output
2 ** 3 = 8

math.pow(2, 200)
1.6069380442589903e+60
2**200
1606938044258990275541962092341162602522202993782792835301376

# positive infinity
float("inf")
# negative infinity
float("-inf")

# ARRAYS/LISTS
# Arrays (or "lists" in python)
You can't do this!
arr = []
arr[0] = 5
arr[1] = 6

Python lists don't auto-expand on index assignment. You must either initialize the list with the required size or use append() to add!
arr = [0] * 2
arr[0] = 5
arr[1] = 6

OR

arr = []
arr.append(5)
arr.append(6)

arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n = [1, 1, 1, 1, 1]
print(arr)
print(len(arr)) = 5

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1]) = 3

# Indexing -2 is the second to last value, etc.
print(arr[-2]) = 2

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3]) = [2, 3]

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4]) = [1, 2, 3, 4]

# But no out of bounds error
print(arr[0:10]) = [1, 2, 3, 4]

# Unpacking
a, b, c = [1, 2, 3] # pattern matching
print(a, b, c)

# Be careful though
# a, b = [1, 2, 3] # error

# Loop through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])
1
2
3

# Without index
for n in nums:
    print(n)
1
2
3


# With index and value
for i, n in enumerate(nums):
    print(i, n)
0 1
1 2
2 3

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
1 2
3 4
5 6

# Reverse
nums = [1, 2, 3]
nums.reverse() = [3, 2, 1] # like nums.reverse! in Ruby
print(nums)

# WRONG!
for n in nums.reverse():
    print(n)

nums.reverse() returns None. Can't loop over it!

# RIGHT:
for n in reversed(nums):
    print(n)

# reversed() and reverse() are used to reverse the order of elements, but differ in their application, return value, and whether they modify the original object.

# 1. list.reverse() Method:
# Applicability: Only for Python lists. Can't with with other iterables like strings or tuples.
# Changes list in-place. Directly changes the order of elements in original list object.
# Returns None. It does not create new list or return reversed version; it simply changes existing list.

# 2. reversed():
# Built-in function for any iterable object: lists, tuples, strings, range, etc.
# Non-destructive: reversed() doesn't change original iterable. Instead, returns a reversed iterator object.
# Returns an iterator that yields the elements of the original iterable in reverse order. To get a new list or tuple, you need to explicitly convert iterator (e.g., using list() or tuple()).

Use list.reverse() when you must reverse a list and no longer need the original order, and you want to save memory by modifying the list directly.

Use reversed() when you must iterate over an iterable in reverse order without changing original, or when working with non-list iterables like strings or tuples.


# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort() = [3, 4, 5, 7, 8] # like arr.sort! in Ruby
print(arr)

arr.sort(reverse=True) = [8, 7, 5, 4, 3]
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort() = ['alice', 'bob', 'doe', 'jane']
print(arr)

# Custom sort (by length of string)
arr.sort(key = lambda x: len(x))
['bob', 'doe', 'jane', 'alice'] # sort by string length

arr.sort(key = lambda x: len(x), reverse = True) # sort by reverse string length
['alice', 'jane', 'bob', 'doe']

> intervals = [[7,10], [2,4], [1, 11]]
> intervals.sort(key = lambda x: x[0]) # sort by 1st element in array
[[1, 11], [2, 4], [7, 10]]
> intervals.sort(key = lambda x: x[1]) # sort by 2nd element in array
[[2, 4], [7, 10], [1, 11]]

# 1. Use list.sort() when:
# You are working with a list.
# You don't need to preserve the original order of the list.
# Memory efficiency is a critical concern, especially with large lists.
# For in-place modification of lists when you don't need the original order

# 2. Use sorted() when:
# You need to sort any iterable (not just lists).
# You need to preserve the original iterable's order.
# You prefer a more functional approach that produces new data rather than modifying existing data.
# For generating new sorted list from any iterable while preserving original, giving greater flexibility.

# Sort hash by keys, then values
scores = {
  "Bob": 85,
  "Eve": 92,
  "Alice": 78,
  "David": 92,
  "Charlie": 85
}

> scores.sort() <--- WRONG! Hash isn't list. Must use sorted().

> sorted_keys = sorted(scores)
> print(f"Sorted by keys: {sorted_keys}")
['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Sort by values first (ascending score), then keys (ascending names) for any tied scores.
> sort_by_score_then_name = sorted(scores.items(), key=lambda item: (item[1], item[0]))
[('Alice', 78), ('Bob', 85), ('Charlie', 85), ('David', 92), ('Eve', 92)]

# Sort by values first (descending score), then keys (ascending names) for ties
> sort_by_score_desc_then_name = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
[('David', 92), ('Eve', 92), ('Bob', 85), ('Charlie', 85), ('Alice', 78)]

# OR
# def sort_key(item):
#     word, count = item
#     return (-count, word)

# sort_by_score_desc_then_name = sorted(scores.items(), key=sort_key)

## List comprehension

# instead of saying:
for name, count in sort_by_score_desc_then_name[:3]
    name

# you can say:
> [name for name, count in sort_by_score_desc_then_name[:3]] <--- [:k] gives first k items from list
['David', 'Eve', 'Bob']


arr = [i for i in range(5)] = [0, 1, 2, 3, 4]
arr = [2*i for i in range(5)] = [0, 2, 4, 6, 8]

## 3 ways to filter list:
1. list comprehension:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in nums if num % 2 == 0]

2. filter():
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda num: num % 2 == 0, nums))

def is_even(num):
    return num % 2 == 0

iterator = filter(is_even, nums)
evens = list(iterator)

3. for loop:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)


# 2-D lists
arr = [[0] * 4 for i in range(2)] = [[0, 0, 0, 0], [0, 0, 0, 0]] # <--- 4 = cols, 2 = rows
arr[1][2]     = 3 => arr = [[0, 0, 0, 0], [0, 0, 3, 0]]
arr[row][col]

# This won't work
# arr = [[0] * 4] * 4 <---- each of these 4 rows will be same! Changing 1 col in 1 row changes same col in all 4 rows!

# STRINGS are like arrays, but they are IMMUTABLE!
s = "abc" # <--- may be single ('') or double quotes ("")
s[0:2] = "ab"
s[0] = "A" # <--- gives ERROR: 'str' object does not support item assignment

# So this creates a new string
s = "abc"
s += "def"
print(s) = "abcdef"

# Valid numeric strings can be converted
print(int("123") + int("123")) = 246

# And numbers can be converted to strings
print(str(123) + str(123)) = "123123"

# In rare cases you may need the ASCII value of a char
print(ord("a")) = 97
print(ord("b")) = 98

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print(" ".join(strings)) = "ab cd ef"

# QUEUES
from collections import deque # this is "double-ended", or items may be added/removed from either front/rear

queue = deque()
queue.append(1) => deque([1])
queue.append(2) => deque([1, 2])
queue.popleft() => removes 1 from left => queue = dequeue([2])

queue.appendleft(1) => adds 1 back from left => deque([1, 2])
queue.pop() => removes 2 from right => deque([1])

# HASHSETS
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet) = {1, 2}
print(len(mySet)) = 2

print(1 in mySet) = True
print(2 in mySet) = True
print(3 in mySet) = False

mySet.remove(2) = {1}
print(2 in mySet) = False

# list to set
print(set([1, 2, 3])) = {1, 2, 3}

# Set comprehension
mySet = { i for i in range(5) } = {0, 1, 2, 3, 4}

# HASHMAPS

# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap) = {'alice': 88, 'bob': 77}
print(len(myMap)) = 2

myMap["alice"] = 80
print(myMap["alice"]) = 80

print("alice" in myMap) = True

myMap.pop("alice") = 80
or del myMap["alice"]  <--- either way deletes key "alice"

print("alice" in myMap) = False

myMap = { "alice": 90, "bob": 70 }
print(myMap) = {'alice': 90, 'bob': 70}

# Dict comprehension
myMap = { i: 2*i for i in range(3) } = {0: 0, 1: 2, 2: 4}

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])
alice 90
bob 70

for val in myMap.values():
    print(val)
90
70

for key, val in myMap.items():
    print(key, val)
alice 90
bob 70

# TUPLES
# like arrays, but immutable

tup = (1, 2, 3)
tup[0] = 1
tup[-1] = 3

tup[0] = 5 <--- error

# can be used as key for hash map/set
myMap = { (1,2): 3 }
myMap[(1,2)] = 3

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet) = True

# Lists can't be keys
myMap[[3,4]] = 5 <--- error

# HEAPS: under the hood, they're arrays

import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
minHeap = [2, 3, 4]

# Min value always at index 0
minHeap[0] = 2

while len(minHeap):
    print(heapq.heappop(minHeap))
2
3
4

# No max heaps by default. Instead, use min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

maxHeap = [-4, -2, -3]

# max is always at index 0
-maxHeap[0] = 4

while len(maxHeap):
    print(-heapq.heappop(maxHeap))
4
3
2

# Now Python 3.14 has maxHeap functions!!
# Each new item pushed into maxHeap automatically resorts to keep max item at 0 element
maxHeap = []
heapq.heappush_max(maxHeap, 3) # Push the value item onto the max-heap heap, maintaining max-heap invariant.
heapq.heappush_max(maxHeap, 2)
heapq.heappush_max(maxHeap, 4)
maxHeap = [4, 2, 3]
maxHeap[0] = 4
while len(maxHeap):
    print(heapq.heappop_max(maxHeap)) # Pop and return the largest item from the max-heap heap
4
3
2


# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
arr = [1, 2, 8, 4, 5]

while arr:
    print(heapq.heappop(arr))

1
2
4
5
8

arr = [2, 1, 8, 4, 5]
heapq.heapify_max(arr)
arr = [8, 5, 2, 4, 1]

# FUNCTIONS

def myFunc(n, m):
    return n * m

myFunc(3, 4) = 12

# Nested/inner functions can access outer variables
def outer(a, b):
    c = 'c'

    def inner():
        return a + b + c
    return inner()

outer('a', 'b') = 'abc'
outer(1, 2) <--- error!

arr = [8, 5, 2, 4, 1]

# Can modify objects but not reassign, unless using nonlocal keyword
def double(arr, val):
    def helper():
        # changing array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # only changes val in helper scope
        # val *= 2 <-- Error! UnboundLocalError: cannot access local variable 'val' where it is not associated with a value

        # changes val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

print(arr, 5) = [16, 10, 4, 8, 2] 10
________
# If you use the nonlocal keyword, the variable will belong to the outer function:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) = "hello"
________
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

Inner: local
Outer: enclosing
Global: global

# Decorator Functions
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction(): # <--- myfunction() is decorated with changecase()
  return "Hello Sally"

@changecase
def otherfunction(): # <--- otherfunction() is decorated with changecase()
  return "I am speed!"

print(myfunction()) = "HELLO SALLY"
print(otherfunction()) = "I AM SPEED!"

# CLASSES

class MyClass:
    # constructor
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    # self keyword required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

obj = MyClass([1, 2, 3])
obj.getLength() = 3
obj.getDoubleLength = 6
