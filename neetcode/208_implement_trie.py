# Trie aka "Prefix Tree"
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# https://neetcode.io/solutions/implement-trie-prefix-tree
# Trie: Walk 1 character at a time

        #   (root)
        #   /    \
        # 'c'    'd'
        #  |       |
        # 'a'     'o'
        #  |       |
        # 't'*    'g'*  <--- * means eow (end of word) is True

# trie
#  │
#  ▼
# (root)  <---- "self" IS "root" node
# root.children = {
#     'c': <Trie node for 'c'>,
#     'd': <Trie node for 'd'>
# }

# After trie.insert('cat'), data structure looks like:

# trie
#  │
#  ▼
# (root)
# children = {
#     'c' ─►  (c)
# }
# eow = False

#             (c) Trie node:
#             children = {
#                 'a' ─►  (a)
#             }
#             eow = False

#                         (a) Trie node:
#                         children = {
#                             't' ─►  (t)
#                         }
#                         eow = False

#                                     (t) Trie node:
#                                     children = {}
#                                     eow = True


# All Trie operations use same traversal:
# 1. Walk 1 character at a time.
# 2. Move curr to the matching child.
# 3. Only the handling of missing children and the ending differs.

class Trie:

    def __init__(self):
        self.children = {}  # key = chars, vals = Trie objects
        self.eow = False    # end of word

    # Walk down the Trie one character at a time.
    # If child doesn't exist, create new Trie node.
    # Move curr to that child.
    # After last character, mark end of word.

    # Time: O(L), Space: O(L) worst case. L = length of input word/prefix
    def insert(self, word: str) -> None:
        curr = self         # "self" IS "root" node above all other inserted words!
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]

        curr.eow = True

    # Walk down the Trie.
    # If any character is missing, return False.
    # After last character, return eow.

    # Time: O(L), Space: O(1)
    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.eow

    # Same as search(), but don't check eow.
    # Reaching last prefix character, return True.

    # Time: O(L), Space: O(1)
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

    trie.insert("app")
    assert trie.search("app") is True

    trie = Trie()

    trie.insert("dog")
    assert trie.search("dog") is True
    assert trie.search("do") is False
    assert trie.startsWith("do") is True

    trie.insert("do")
    assert trie.search("do") is True

    trie.insert("card")
    trie.insert("cards")
    assert trie.search("car") is False
    assert trie.search("cards") is True
    assert trie.search("card") is True
    assert trie.startsWith("car") is True

    print("All tests passed!")
