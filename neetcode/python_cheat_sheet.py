# Python Cheat Sheet: quick Python review
# https://neetcode.io/courses/lessons/python-for-coding-interviews
# Even better: https://static.realpython.com/python-cheatsheet.pdf

# VARIABLES

# are dynamically typed
n = 0
print("n =", n)
>>> n = 0

n = "abc"
print("n =", n)
>>> n = abc

# String interpolation
name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}') # may be single or double quotes
>>> Hello World! This is Python

a = 12
b = 3
print(f'12 multiply 3 is {a * b}.')
>>> 12 multiply 3 is 36.

# >>> n = abc

# Multiple assignments
n, m = 0, "abc"
n, m, z = 0.125, "abc", False

# None is null (absence of value)
n = 4
n = None
print("n =", n)
>>> n = None

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

Output for n: 3

# LOGICAL OPERATORS: and, or, not.
# Python runs operations in this order: not, and, or.
# Parentheses needed for multi-line conditions.

n, m = 1, 2
if (n > 2 and n != m) or n == m:
    n += 1

# LOOPS

n = 5
while n < 5:
    print(n)
    n += 1

# Looping from i = 0 to 4
for i in range(5):
    print(i)

# Looping from i = 2 to 5
for i in range(2, 6):
    print(i)

# Looping from i = 5 to 2
for i in range(5, 1, -1):
    print(i)

# Loop through collection:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through collection with index:
for i in range(len(fruits)):
    print(i, fruits[i])

# Loop through collection with index and value:
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry

colors = ["red", "yellow", "purple"]

# Loop through multiple collections simultaneously:
for fruit, color in zip(fruits, colors):
    print(fruit, color)

# Output:
# apple red
# banana yellow
# cherry purple

# MATH

# Division is decimal by default
5/2
>>> 2.5

# Double slash mean "floor division." Results round DOWN to nearest integer.
 3 // 2  = 1 #  1.5 rounds down to 1
-3 // 2 = -2 # -1.5 rounds down to -2

# A workaround to round towards 0: Use decimal division, then convert to int
int(-3/2)
>>> -1
int(1.9)
>>> 1
int(-1.9)
>>> -1

# Remember: a = (a // b) * b + (a % b)

 10 // 3 =  3     |  10 % 3 = 1
-10 // 3 = -4     | -10 % 3 = 2, 10 % -3 = -2 <--- remainder has same sign as divisor


# To match other languages:
import math

math.fmod(-10, 3) = -1
math.floor(3 / 2) = 1   # same as 3 // 2
math.ceil(3 / 2) = 2
math.floor(-3 / 2) = -2 # same as -3 // 2
math.sqrt(2)
math.pow(2, 3) = 8.0    # always gives float output
2 ** 3 = 8

math.pow(2, 200)
1.6069380442589903e+60

2**200 # precise
1606938044258990275541962092341162602522202993782792835301376

# Why doesn't it overflow? Python integers are arbitrary precision integers ("big integers"). They are implemented using a dynamically sized array of digits, allowing them to represent arbitrarily large numbers without overflow.

# A Python int is actually an object that stores:
# - The sign (positive or negative)
# - The number of "digits" needed
# - The digits themselves

# But Python floats DO overflow. Python floats are IEEE 754 double precision floating-point numbers, implemented with 64-bit binary representation, which can only represent a finite range of numbers (15-17 decimal digits of precision).

# 64 bits total:
# 1 sign bit
# 11 exponent bits
# 52 fraction bits

2.0**1024
>>> OverflowError: (34, 'Result too large')

# ARRAYS (or "LISTS" in python)

# Python lists don't auto-expand on index assignment. You must either initialize list with its required size or use append() to add!
arr = [0] * 3
>>> [0, 0, 0]

arr[0] = 5
arr[1] = 6

OR

arr = []
arr.append(5)
arr.append(6)
>>> [5, 6]

arr = [1, 2, 3]
print(arr)

# Using list as a stack
arr.append(4)
arr.append(5)
>>> [1, 2, 3, 4, 5]

arr.pop()
>>> [1, 2, 3, 4]

arr.insert(1, 7)
>>> [1, 7, 2, 3, 4]

arr[0] = 0
arr[3] = 1
>>> [0, 7, 2, 1, 4]

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n = [1, 1, 1, 1, 1]
print(arr)
print(len(arr)) = 5

# Index -1 is not out of bounds. It's the last array element.
arr = [1, 2, 3]
arr[-1]
>>> 3

# Indexing -2 is second to last value, etc.
arr[-2]
>>> 2

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
arr[1:3]
>>> [2, 3]

# Like for-loop ranges, last index is not included
arr[0:4]
>>> [1, 2, 3, 4]

# But no out of bounds error if last index > list length
arr[0:10]
>>> [1, 2, 3, 4]

# Unpacking
a, b, c = [1, 2, 3] # pattern matching
print(a, b, c)
>>> 1 2 3

# Pattern matching: number of variables must equal number of values
a, b = [1, 2, 3]
>>> ValueError: too many values to unpack (expected 2, got 3)

# Loop through arrays...
nums = [1, 2, 3]

# With index
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
____________________
# reverse() and reversed()

nums = [1, 2, 3]
nums.reverse() # same as nums.reverse! in Ruby
>>> [3, 2, 1]

# WRONG!
for n in nums.reverse():
    print(n)

nums.reverse() returns None. Can't loop over it!

# RIGHT: "reversed()" returns an iterator, so we CAN loop over it
for n in reversed(nums):
    print(n)

OR

for i in range(len(nums) - 1, -1, -1):
    print(nums[i])

# reversed() and reverse() are used to reverse the order of elements, but differ in application, return value, and if they modify the original object.

# 1. list.reverse() method:
# Only for Python lists. Can't use with with other iterables like strings or tuples.
# Changes list in-place. Directly changes order of elements in original list object.
# Returns "None". It does not create new list or return reversed version; it simply changes existing list.

# WRONG!
# for n in nums.reverse():
#     print(n)

# nums.reverse() returns None. Can't loop over it!

# 2. reversed():
# Built-in function for any iterable (lists, tuples, strings, range, etc.).
# Non-destructive: reversed() doesn't change original iterable. Instead, returns a reversed iterator object.

# RIGHT:
# for n in reversed(nums):
#     print(n)

# Returns an iterator that yields the elements of original iterable in reverse order. To get a new list or tuple, you must explicitly convert iterator (e.g., using list() or tuple()).

Use list.reverse() when you must reverse a list and no longer need its original order, and you want to save memory by modifying the list directly.

nums = [1,2,3]
x = nums.reverse()
nums
>>> [3, 2, 1]
print(x)
>>> None

Use reversed() when you must ITERATE over an iterable in reverse order without changing original, or when working with non-list iterables like strings or tuples.

nums = [1,2,3]
r = reversed(nums)
r
>>> <list_reverseiterator object at 0x7f5117847310>
list(r)
>>> [3, 2, 1]

reversed() works on more than lists:

s = "hello"
r = reversed(s)
list(r)
>>> ['o', 'l', 'l', 'e', 'h']

t = (1, 2, 3) # tuples are immutable, so reversed() returns a new tuple
for x in reversed(t):
    print(x)
3
2
1

list(reversed(t))
>>> (3, 2, 1)

____________________
# sort() and sorted()

arr = [5, 4, 7, 3, 8]
arr.sort() # same as arr.sort! in Ruby
>>> [3, 4, 5, 7, 8]

arr.sort(reverse=True)
>>> [8, 7, 5, 4, 3]

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
>>> ['alice', 'bob', 'doe', 'jane']

# Custom sort (by length of string)
arr.sort(key = lambda x: len(x))
['bob', 'doe', 'jane', 'alice'] # sort by string length

arr.sort(key = lambda x: len(x), reverse = True) # sort by reverse string length
['alice', 'jane', 'bob', 'doe']

intervals = [[7,10], [2,4], [1, 11]]
intervals.sort(key = lambda x: x[0]) # sort by 1st element in array
>>> [[1, 11], [2, 4], [7, 10]]
intervals.sort(key = lambda x: x[1]) # sort by 2nd element in array
>>> [[2, 4], [7, 10], [1, 11]]

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

# Sort hash (aka "dict") by keys, then values
scores = {
  "Bob": 85,
  "Eve": 92,
  "Alice": 78,
  "David": 92,
  "Charlie": 85
}

scores.sort() # WRONG! Hash isn't list. Must use sorted().

sorted_keys = sorted(scores)
sorted_keys
>>> ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Sort by values first (ascending score), then keys (ascending names) for any tied scores.
sort_by_score_then_name = sorted(scores.items(), key=lambda item: (i[1], i[0]))
>>> [('Alice', 78), ('Bob', 85), ('Charlie', 85), ('David', 92), ('Eve', 92)]

# Sort by values first (descending score), then keys (ascending names) for ties
sort_by_score_desc_then_name = sorted(scores.items(), key=lambda item: (-i[1], i[0]))
>>> [('David', 92), ('Eve', 92), ('Bob', 85), ('Charlie', 85), ('Alice', 78)]

# OR same thing, using function:

def sort_key(item):
    word, count = item
    return (-count, word)

sort_by_score_desc_then_name = sorted(scores.items(), key=sort_key)
>>> [('David', 92), ('Eve', 92), ('Bob', 85), ('Charlie', 85), ('Alice', 78)]

__________________________
# List Comprehension

[i for i in range(5)]
>>> [0, 1, 2, 3, 4]

[2*i for i in range(5)]
>>> [0, 2, 4, 6, 8]

# instead of:
for name, count in sort_by_score_desc_then_name[:3]:
    name

# you can say:
[name for name, count in sort_by_score_desc_then_name[:3]] # [:k] gives first k items from list
>>> ['David', 'Eve', 'Bob']

## 3 ways to filter list:
1. list comprehension:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in nums if num % 2 == 0]
>>> [2, 4, 6, 8, 10]

2. filter():

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda num: num % 2 == 0, nums))
>>> [2, 4, 6, 8, 10]

# OR same thing, using function:

def is_even(num):
    return num % 2 == 0

iterator = filter(is_even, nums)
evens = list(iterator)
>>> [2, 4, 6, 8, 10]

3. for loop:

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
>>> [2, 4, 6, 8, 10]

# 2D lists

# Make 2D list, all 0's, with rows x cols
arr = [[0] * rows for i in range(cols)]

arr = [[0] * 4 for i in range(2)] # 4 = cols, 2 = rows
>>> [[0, 0, 0, 0], [0, 0, 0, 0]]

arr[1][2] = 3 # arr[r][c]
>>> [[0, 0, 0, 0], [0, 0, 3, 0]]

# This won't work
# arr = [[0] * 4] * 4 <---- each of these 4 rows will be same! Changing 1 col in 1 row changes same col in all 4 rows!

__________________________
# STRINGS are like arrays, but they are IMMUTABLE!

s = "abc" # <--- may be single ('') or double quotes ("")
s[0:2] = s[:2] = "ab"
s[1:3] = s[1:] = "bc"
s[2:4] = s[2:] = "c"
s[0] = "A" # <--- gives ERROR: 'str' object does not support item assignment

# This creates a new string
s = "abc"
s += "def"
print(s) = "abcdef"

# Valid numeric strings can be converted
int("123") + int("123")
>>> 246

# Numbers can be converted to strings
str(123) + str(123)
>>> "123123"

# ASCII value of a char
ord('A')
>>> 65
ord('a')
>>> 97
ord('b')
>>> 98

# Combine list of strings (with an empty string delimiter)
strings = ['ab', 'cd', 'ef']
' '.join(strings)
>>> 'ab cd ef'
_____________________
# QUEUES

# This is "double-ended." Items may be added/removed from either front/rear
from collections import deque

queue = deque()
queue.append(1)
>>> deque([1])
queue.append(2)
>>> deque([1, 2])
queue.popleft() # removes "1" from left
>>> deque([2])
queue.appendleft(1) # adds "1" to left
>>> deque([1, 2])
queue.pop() # removes "2" from right
>>> deque([1])
_____________________
# HASHSETS (sets): like arrays, but unordered + unique values

mySet = set()

mySet.add(1)
>>> {1}
mySet.add(2)
>>> {1, 2}
mySet.add(1) # adding duplicate value does nothing
>>> {1, 2}
len(mySet)
>>> 2

1 in mySet
>>> True
2 in mySet
>>> True
3 in mySet
>>> False

mySet.remove(2)
>>> {1}
2 in mySet
>>> False

# change list to set
set([1, 2, 3])
>>> {1, 2, 3}

# Set comprehension
mySet = { i for i in range(5) }
>>> {0, 1, 2, 3, 4}
_____________________
# HASHMAPS (dicts): key-value pairs. Keys are unique and unordered

myMap = {}
myMap['alice'] = 88
myMap['bob'] = 77
myMap
>>> {'alice': 88, 'bob': 77}
len(myMap)
>>> 2

myMap['alice'] = 80
myMap['alice']
>>> 80

'alice' in myMap
>>> True

myMap.pop('alice')
>>> 80
myMap
>>> {'bob': 77}

OR

del myMap['alice']  # either way deletes key "alice"

'alice' in myMap
>>> False

myMap = { "alice": 90, "bob": 70 }
myMap
>>> {'alice': 90, 'bob': 70}

# Dict comprehension
myMap = { i: 2*i for i in range(3) } = {0: 0, 1: 2, 2: 4}

# Looping through maps
myMap = { "alice": 90, "bob": 70 }

for key, val in myMap.items():
    print(key, val)

>>> alice 90
>>> bob 70

for key in myMap:
    print(key, myMap[key])

>>> alice 90
>>> bob 70

for val in myMap.values():
    print(val)

>>> 90
>>> 70
_____________________
# TUPLES: like arrays, but immutable

tup = (1, 2, 3)
tup[0]
>>> 1
tup[-1]
>>> 3

# Can't modify tuples
tup[0] = 5 <--- error

# Tuples may be key for map
myMap = {(1, 2): 3}
myMap[(1,2)]
>>> 3

# Lists may NOT be keys. Only immutable objects may be keys.
myMap[[3,4]] = 5 # Error: cannot use 'list' as a dict key (unhashable type: 'list')
myMap['Ray'] = 10 # OK: string is immutable

# We may add tuple to set ONLY if tuple's items are immutable: integers, strings, other valid tuples.
# If tuple has any mutable items: lists, dictionaries, sets, etc. it may NOT be added to set.
mySet = set()
mySet.add((1, 2))

(1, 2) in mySet
>>> True

mySet.add([2, 3]) # Error: unhashable type: 'list'
mySet.add({2: 3}) # Error: unhashable type: 'dict'
mySet.add((1, (2, 3))) # OK: tuple is immutable
_____________________
# HEAPS: under the hood, they're arrays

import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
>>> [2, 3, 4]

# Min value is always at index 0 of heap
minHeap[0] = 2

while minHeap:
    print(heapq.heappop(minHeap))
2
3
4

while len(minHeap):
    print(heapq.heappop(minHeap))
2
3
4

# Before Python 3.14: No max heaps by default. Instead, use min heap and multiply each element by -1 when push & pop.
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

# Python 3.14 has maxHeap functions (heappush_max, heappop_max, heapify_max)
# Each new item pushed into maxHeap automatically keeps max item at 0 element
maxHeap = []
heapq.heappush_max(maxHeap, 3) # Push the value item onto the max-heap heap, maintaining max-heap invariant.
heapq.heappush_max(maxHeap, 2)
heapq.heappush_max(maxHeap, 4)
maxHeap = [4, 2, 3]
maxHeap[0] = 4
while len(maxHeap):
    print(heapq.heappop_max(maxHeap)) # Pop and return largest item from max heap
4
3
2


# Build heap from initial values

arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
arr = [1, 2, 8, 4, 5] # min heap

while arr:
    print(heapq.heappop(arr))
1
2
4
5
8

arr = [2, 1, 8, 4, 5]
heapq.heapify_max(arr)
arr = [8, 5, 2, 4, 1] # max heap
_____________________________
# FUNCTIONS

def myFunc(n, m):
    return n * m

myFunc(3, 4)
>>> 12

# Nested/inner functions can access outer variables
def outer(a, b):
    c = 'c'

    def inner():
        return a + b + c
    return inner()

outer('a', 'b')
>>> 'abc'

arr = [8, 5, 2, 4, 1]

# Can modify objects but not reassign, unless using nonlocal keyword
def double(arr, val):
    def helper():
        # changing array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # this tries to change val in helper() scope, but val is undefined!
        # val *= 2 # Error! Cannot access local variable 'val' where it is not associated with a value

        # with "nonlocal" keyword, val now refers to val in outer function scope. now it can be changed
        nonlocal val
        val *= 2

    helper()
    print(arr, val)

print(arr, 5)
>>> [16, 10, 4, 8, 2] 10

def myfunc1():
  x = "Jane"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

myfunc1()
>>> "Jane"

# Nonlocal keyword on x means it belongs to outer myfunc1() scope:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

myfunc1()
>>> "hello"
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

>>> Inner: local
>>> Outer: enclosing
>>> Global: global
________
# Decorator Functions: A decorator wraps a function, changing its behavior.
# It takes another function as input and returns a new function.
# https://realpython.com/primer-on-python-decorators/

def decorator(func):
    def wrapper():
        print("Something happens before calling function")
        func()
        print("Something happens after calling function")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)

say_whee()
>>> Something happens before calling function
>>> Whee!
>>> Something happens after calling function

# Add syntactical sugar to apply decorator to function:

@decorator # means same as "say_whee = decorator(say_whee)"
def say_whee():
    print("Whee!")

say_whee()
>>> Something happens before calling function
>>> Whee!
>>> Something happens after calling function
_____________________________
# CLASSES
# https://realpython.com/python3-object-oriented-programming/
# https://realpython.com/python-classes/

class MyClass:
    # constructor
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    # self keyword required as param
    def get_length(self):
        return self.size

    def get_double_length(self):
        return 2 * self.get_length()

obj = MyClass([1, 2, 3])
obj.get_length()
>>> 3
obj.get_double_length()
>>> 6
_____________________________
# 4 ways to make freq hash of a list:

nums = [2, 1, 3, 2, 3, 0, 2]
freq = {}

# 1. Easy to remember, but slow to type

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

freq
>>> {2: 3, 1: 1, 3: 2, 0: 1}

# 2. ** Preferred Way **

for n in nums:
    # dict.get(key, default) ---
    # if key exists, give value of hashmap, else give default value (0 here)
    freq[n] = freq.get(n, 0) + 1

freq
>>> {2: 3, 1: 1, 3: 2, 0: 1}

# 3. Counter. If you only need to count frequencies.

from collections import Counter
freq = Counter(nums)

freq
>>> Counter({2: 3, 3: 2, 1: 1, 0: 1})

Counter('mississippi')
>>> Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Useful method: most_common(k). Useful for "Top K Frequent Elements."
freq.most_common(1)
>>> [(2, 3)]

freq.most_common(3)
>>> [(2, 3), (3, 2), (1, 1)]


# 4. defaultdict

from collections import defaultdict
freq = defaultdict(int)
for n in nums:
    freq[n] += 1

freq
>>> defaultdict(<class 'int'>, {2: 3, 1: 1, 3: 2, 0: 1})

# defaultdict automatically gives default value to keys that don't exist
# defaultdict(int) default val = 0
# defaultdict(list) default val = []
# defaultdict(str) default val = ""

# When is advantage to use defaultdict?

# a. Grouping: To group elements by key + don't want to check if key exists, plus no need to set default values.

Instead of:

groups = {}
for word in words:
    key = len(word)

    if key not in groups:
        groups[key] = []
    groups[key].append(word)

You can do:

groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word) # much clearer

# b. Graph adjacency lists

Instead of:

graph = {}
for u, v in edges:
    if u not in graph:
        graph[u] = []

    graph[u].append(v)

You can do:

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
