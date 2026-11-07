# https://leetcode.com/problems/word-ladder/
# https://neetcode.io/solutions/word-ladder
# BFS with levels (since each BFS level is 1 letter change)

# Don't ask "Is word A connected to word B?"
# Ask "What are all possible valid words we can make by changing 1 letter of word A?"

# Add each word in wordList to wildcard dictionary.
# Then we can look up all a word's neighbors in O(1) time.
# For first test, wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
# wdict = {
#   '*og': {'cog', 'dog', 'log'},
#   '*ot': {'lot', 'dot', 'hot'},
#   'c*g': {'cog'},
#   'co*': {'cog'},
#   'd*g': {'dog'},
#   'd*t': {'dot'},
#   'do*': {'dot', 'dog'},
#   'h*t': {'hot'},
#   'ho*': {'hot'},
#   'l*g': {'log'},
#   'l*t': {'lot'},
#   'lo*': {'lot', 'log'}
# }

from collections import deque
# N = number of words, L = length of each word
# Time: O(N * L^2)
# Space: O(N * L^2)
def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList:
        return 0

    wdict = {}
    for word in wordList:
        for i in range(len(word)):
            # make wildcard version of word with '*' at index i
            pattern = word[:i] + '*' + word[i+1:]
            # word  = word[:i] + word[i:]
            # 'hit' = word[:1] + word[1:] = 'h' + 'it'
            # 'h*t' = word[:1] + '*' + word[2:] = 'h' + '*' + 't'
            # '*it' = word[:0] + '*' + word[1:] = '' + '*' + 'it'
            # 'hi*' = word[:2] + '*' + word[3:] = 'hi' + '*' + ''

            # wdict.setdefault(pattern, set()).add(word) means same as next 3 lines:
            if pattern not in wdict:
                wdict[pattern] = set()
            wdict[pattern].add(word)

    q = deque([beginWord])
    steps = 1
    visited = {beginWord} # set()
    # Don't do set(beginWord), since that adds string 1 character at a time to set.

    while q:
        size = len(q)

        for _ in range(size):
            word = q.popleft()
            if word == endWord:
                return steps    # Found shortest sequence!

            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]

                # Don't say "for neighbor in wdict[pattern]:" since it may
                # seek patterns (like "*it" and "hi*") that are NOT in wdict.
                # Since we used wordList to make wdict, excluding beginWord, this happens.

                # To use "for neighbor in wdict[pattern]:", must also add lines like
                # allWords = wordList.copy()
                # allWords.append(beginWord), then use "for word in allWords:" to make wdict.

                for neighbor in wdict.get(pattern, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        steps += 1

    return 0    # never found endWord

if __name__ == "__main__":
    # A good shortest transformation sequence is
    # "hit" -> "hot" -> "dot" -> "dog" -> cog",  5 words long.
    assert ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    # endWord must be in wordList, but it doesn't have to be the last word.
    assert ladderLength("hit", "cog", ["hot","dot","dog","cog","lot","log"]) == 5

    assert ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0

    # could use "cat" -> "bat" -> "bag" -> "sag", 4 words
    assert ladderLength("cat", "sag", ["bat","bag","sag","dag","dot"]) == 4
    assert ladderLength("cat", "sag", ["bat","bag","sat","dag","dot"]) == 0
    print("All tests passed!")

#----- To find full sequence of words we used to find endWord: ----------------

# 1. Add parent dictionary. key = word, value = word just before it.

# parent = {beginWord: None}

# then when we discover a new neighbor,

# if neighbor not in visited:
#     visited.add(neighbor)
#     parent[neighbor] = word  # Remember where we came from
#     q.append(neighbor)

# For first test, parent dictionary could be:

# parent = {
#     "hit": None,
#     "hot": "hit",
#     "dot": "hot",
#     "lot": "hot",
#     "dog": "dot",
#     "log": "lot",
#     "cog": "dog"
# }

# 2. Reconstruct path to find endWord. Replace:

# if word == endWord:
#     return steps

# with

# if word == endWord:
#     sequence = []
#     curr = endWord

#     while curr is not None:
#         sequence.append(curr)
#         curr = parent[curr]

#     sequence.reverse()
#     print("Shortest sequence:", " -> ".join(sequence))
#     return steps

# This follows the parent pointers backward:

# cog → dog → dot → hot → hit

# Then reverses them:

# hit → hot → dot → dog → cog
