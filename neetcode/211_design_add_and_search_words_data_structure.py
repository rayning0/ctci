# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# https://neetcode.io/problems/design-word-search-data-structure/solution
# Trie: DFS Wildcard Search

# See https://github.com/rayning0/ctci/blob/master/neetcode/208_implement_trie.py

# When search for wildcard character ('.') for curr node, don't just search 1 path.
# We must use DFS to search ALL curr.children values!

class WordDictionary:
    def __init__(self):
        self.children = {}
        self.eow = False

    # Time: O(L), Space: O(L) worst case. L = length of input word/prefix
    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]

        curr.eow = True

    # Time: O(L) average, O(26^L) worst case if every character is '.'
    # Space: O(L) recursion depth. L = length of search word
    def search(self, word: str) -> bool:

        # Can this subtree match word[i:] ?
        def dfs(curr, i):
            # Finished matching the whole word. Base case.
            if i == len(word):
                return curr.eow

            c = word[i]

            # Wildcard: try every child.
            if c == '.':
                for child in curr.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            # Normal character.
            if c not in curr.children:
                return False

            return dfs(curr.children[c], i + 1)

        return dfs(self, 0)

if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')

    assert obj.search("pad") == False
    assert obj.search("bad") == True
    assert obj.search(".ad") == True
    assert obj.search("b..") == True
    print("All tests passed!")

------------Thought process-----------
Step 1. You already know this works in LC 208

```python
curr = self

for c in word:
    if c not in curr.children:
        return False
    curr = curr.children[c]

return curr.eow
```

Then ask yourself

> **What breaks?**

Only one thing:

```text
'.' (wildcard)
```

---

# Step 2. Ask one question

When I see

```text
'.'
```

which child should I follow?

Answer:

```text
I don't know.
```

---

# Step 3.

If I don't know,

what are my choices?

Suppose

```text
(a)
 / | \
t r n
```

Searching

```text
ca.
```

means

```text
Could be

cat
car
can
```

So the algorithm becomes

```text
Try 't'

If that fails,
try 'r'

If that fails,
try 'n'
```

Immediately you should think

```text
Backtracking
DFS
```

---

# Step 4.

Ask

> What information must DFS know?

Not much.

Only

1. where I am (index i)

2. what character I'm matching next

So

```python
dfs(node, i)
```

is almost forced.

---

# Step 5.

Now define exactly what dfs means.
This is the hardest step.

```text
dfs(node, i)

=

Can this subtree match word[i:] ?
```

This one sentence determines almost the whole function.

---

# Step 6.

Derive the base case. Suppose

```text
word = "cat"
```

Eventually

```text
i == 3
```

What question remains?

Only

> Did I end exactly at the end of a stored word?

Therefore

```python
if i == len(word):
    return node.eow
```

The base case almost writes itself.

---

# Step 7.

Now consider exactly one character.

```python
c = word[i]
```

There are only two possibilities.

---

Normal character

```text
c != '.'
```

Exactly one path. Same as LC 208.

---

Wildcard

```text
c == '.'
```

Many paths.

---

# Step 8.

How do I try every path?

You already know.

```python
for child in node.children.values():
```

---

# Step 9.

Suppose one child works. What do I return?

Immediately

```python
return True
```

Otherwise (no child works)

```python
return False
```

Done.

---

The final algorithm almost writes itself from 4 questions.

```text
1. What does dfs mean?

Can this subtree match word[i:]?

↓

2. What's the base case?

Matched whole word?

↓

3. One child or many?

Normal char
vs
'.'

↓

4. If many?

Try every child.
```

That's literally the entire solution.

---
Instead of memorizing code, memorize the evolution.

### Version 1

LC 208

```text
Walk exactly 1 path.
```

↓

### Version 2

Oops.

```text
'.'

means

I don't know which path.
```

↓

### Version 3

```text
Try every path.
```

↓

### Version 4

Trying every path

=

DFS.

↓

### Version 5

DFS needs

```python
(node, i)
```

↓

### Version 6

Define

```text
dfs(node, i)

=

Can this subtree match word[i:]?
```

Everything else follows naturally.

---

The key insight isn't the wildcard. It's choosing the right contract:

> `dfs(node, i)` returns if the subtree rooted at `node` can match the remaining suffix `word[i:]`

Once you state that contract clearly, the base case and the recursive cases become almost inevitable. That's the habit to keep practicing: before writing any recursive code, write down exactly what the recursive function is supposed to mean. It's the single biggest step toward deriving these solutions instead of memorizing them.
