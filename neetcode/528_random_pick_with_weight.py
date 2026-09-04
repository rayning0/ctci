# https://leetcode.com/problems/random-pick-with-weight/
# https://neetcode.io/solutions/random-pick-with-weight
# Prefix Sum + Lower Bound Binary Search

# 1. Prefix sum + Binary search

# PLAN:
# 1. Build prefix sum array of the weights. For w = [1, 3, 2], prefix sums would be [1, 4, 6].
# 2. Generate random number target in [1, total_sum].
# 3. Find first index in prefix sum array where cumulative sum ≥ target. <-- LOWER BOUND binary search
import random
class Solution:
    # Time: O(n), Space: O(n)
    def __init__(self, w: list[int]):
        self.prefix = [0] * len(w)
        self.prefix[0] = w[0]
        for i in range(1, len(w)):
            self.prefix[i] = self.prefix[i - 1] + w[i]

    # Time: O(log n), Space: O(1)
    def pickIndex(self) -> int:
        total_sum = self.prefix[-1]             # last item in prefix sum array is total sum
        target = random.randint(1, total_sum)

        # LOWER BOUND binary search
        l, r = 0, len(self.prefix)
        while l < r:
            mid = (l + r) // 2
            if self.prefix[mid] >= target:
                r = mid
            else:
                l = mid + 1

        return l
______________________
Q: Why Prefix Sum Approach Works:

The prefix sum converts weights into contiguous ranges on a number line. A uniform random pick on that line naturally lands in each range with probability proportional to its size (weight). Binary search efficiently finds which range the pick fell into.

Think of it as a number line divided into segments:

Example: w = [1, 3, 2], total = 6
Index 0     Index 1        Index 2
[--1--][---2---3---4---][---5---6---]
   ↑                      ↑
  1 slot               2 slots
         ↑
       3 slots

Each index gets a segment whose length equals its weight:

Index 0 occupies: [1] → length 1
Index 1 occupies: [2, 3, 4] → length 3
Index 2 occupies: [5, 6] → length 2

Key Insight
When you pick a random number "target" uniformly from [1, 6]:

target	        Falls in segment of	    Probability
1	            Index 0	                1/6
2, 3, 4	        Index 1	                3/6
5, 6	        Index 2	                2/6

This matches exactly: P(index i) = w[i] / sum(w) ✅

Q: Why "first prefix sum ≥ target"?

The prefix sum array [1, 4, 6] marks end of each segment:

prefix[0] = 1 → segment for index 0 ends at 1
prefix[1] = 4 → segment for index 1 ends at 4
prefix[2] = 6 → segment for index 2 ends at 6

So if target = 3:

prefix[0] = 1 < 3 ❌ — not this one
prefix[1] = 4 ≥ 3 ✅ — first one that reaches or passes 3 → answer is index 1
The first index where prefix[i] ≥ target is exactly the segment that contains target.

Q: Why should we get random number from 1 to total_sum, not 0 to total_sum? Does it make a difference?

"target = random.randint(1, total_sum)"

Starting from 1 makes each segment's count of integers equal its weight.
Starting from 0 shifts everything and steals a ticket from the last person.

Think of it like a raffle ticket machine 🎟️

w = [1, 3, 2] — Total tickets = 6
You sell tickets numbered 1 through 6:

Person 0 buys ticket:  1           (1 ticket)
Person 1 buys tickets: 2, 3, 4     (3 tickets)
Person 2 buys tickets: 5, 6        (2 tickets)
You draw one random ticket from 1 to 6. Whoever owns that ticket wins.

Person 0 wins if ticket 1 is drawn → 1/6 chance ✅
Person 1 wins if ticket 2, 3, or 4 is drawn → 3/6 chance ✅
Person 2 wins if ticket 5 or 6 is drawn → 2/6 chance ✅

What if we use 0 to 6? (7 tickets)
Person 0 buys ticket:  0           ← this one is extra!
Person 0 also owns:    1
Person 1 owns:         2, 3, 4
Person 2 owns:         5, 6
Now Person 0 has 2 tickets out of 7 → 2/7 instead of 1/6 ❌

Q: What if we use 0 to 5? (6 tickets, but shifted)

Person 0 buys ticket:  0           (1 ticket)
Person 1 buys tickets: 1, 2, 3     (3 tickets)
Person 2 buys tickets: 4, 5        (2 tickets)
Now look at your code's logic: "find the first prefix sum ≥ target"

prefix = [1, 4, 6]
target = 0 → prefix[0] = 1 ≥ 0 → Person 0 ✅
target = 1 → prefix[0] = 1 ≥ 1 → Person 0 ✅ ← Person 0 gets two!
target = 2 → prefix[1] = 4 ≥ 2 → Person 1 ✅
target = 3 → prefix[1] = 4 ≥ 3 → Person 1 ✅
target = 4 → prefix[1] = 4 ≥ 4 → Person 1 ✅
target = 5 → prefix[2] = 6 ≥ 5 → Person 2 ❌ (should be Person 1!)
Person 0 gets 2 picks, Person 2 gets 1 pick — completely wrong.

# 2. Expanded array, with index values repeated based on weights.
# Exceeds memory limit.
import random
class Solution:

    # Time: O(sum(w)). But sum(w) may be up to 10⁴ × 10⁵ = 10⁹. The self.wt list could hold up to 1 billion elements, far exceeding memory limit.
    def __init__(self, w: list[int]):
        self.wt = []

        for i, weight in enumerate(w):
            self.wt.extend([i] * weight)

    # Time: O(1)
    def pickIndex(self) -> int:
        return random.choice(self.wt)

# You built an expanded array where each index i is repeated w[i] times, then used random.choice() to pick uniformly at random.

# for i, weight in enumerate(w):
#     self.wt.extend([i] * weight)

# This is a creative and intuitively correct idea — each index appears proportional to its weight.

# Why It Got Memory Limit Exceeded
# The constraints are:

# w.length up to 10⁴
# w[i] up to 10⁵
# So sum(w) can be as large as 10⁴ × 10⁵ = 10⁹. Your self.wt list could hold up to 1 billion elements, which far exceeds the memory limit.
_____________________
Algorithm Decision Challenge:

You are building a weighted recommendation engine for a large e-commerce platform. The system selects items to recommend to users with probability proportional to each item's relevance score.

System Parameters:

- The catalog contains 10,000 items with relevance scores as positive integers
- Relevance scores vary dramatically — from 1 (niche products) to 100,000 (top sellers), spanning five orders of magnitude
- The recommendation endpoint serves 50,000 requests per second during peak traffic
- Each request must return a result within a strict sub-millisecond latency SLA
- Weights are recalculated once per day via an offline batch job; during the day, they remain static
- The service is maintained by a small team that prioritizes correctness, debuggability, and minimal production risk

[Options]

A. Alias Method — O(n) preprocessing, O(1) per pick

B. Prefix Sum + Binary Search — O(n) preprocessing, O(log n) per pick

C. Linear Scan with Cumulative Sum — O(1) preprocessing, O(n) per pick

D. Expanded Array (flatten weights into individual entries) — O(sum(w)) preprocessing, O(1) per pick

[Option Analysis]

Option	Verdict	                Notes

B ✅	   Correct choice	        O(log n) per pick easily meets sub-ms SLA at n=10,000. Integer arithmetic guarantees exact probabilities. Simple to implement and debug.
A	    Rejected correctly	     O(1) is theoretically faster, but float precision with extreme weight ratios introduces correctness risk. Implementation complexity is unjustified when O(log n) already meets the SLA.
C	    Rejected correctly	     O(n) per pick is fundamentally incompatible with 50K calls/sec at n=10,000.
D	    Rejected correctly	     O(sum(w)) space is a hard blocker — up to 10⁹ elements exceeds memory limits.

[What-If Challenge]

What if scenario changes: the catalog shrinks to only 50 items, but endpoint now serves 5 million requests per second, and the system is a hard real-time embedded controller where worst-case latency must be bounded to under 100 nanoseconds per call.

Would your algorithm choice change? If so, how and why?

This constraint flip makes Option D viable for the first time. But Option A is the true winner of this scenario — it delivers the same O(1) speed as D while using O(n) space instead of O(sum(w)). The original scenario's large n (10,000) and moderate call rate made B the pragmatic choice; shrinking n to 50 and cranking up the frequency flips the trade-off entirely.

With only 50 items, the memory problem that killed Option D before largely disappears, and the extreme call frequency (5M/sec) with a 100ns budget makes raw per-pick speed the top priority.

One nuance to consider: With 50 items and weights up to 100,000, sum(w) could still reach 50 × 100,000 = 5,000,000 — that's a 20MB array (5M × 4 bytes). On an embedded controller, that might still be tight.

This is where Option A (Alias Method) actually becomes the stronger pick in this scenario:

                        Option A (Alias)	                Option D (Expanded)
Per-pick	            O(1) — 2 array lookups + 1 random	O(1) — 1 array lookup + 1 random
Space	                O(n) = 50 entries (~400 bytes)	    O(sum(w)) = up to 5M entries (~20MB)
Float precision risk	Minimal with only 50 items	        None (integer indexing)
Implementation	        Moderate	                        Trivial

With n=50, the Alias Method's complexity is trivial to implement and debug, float precision is a non-issue, and it uses ~50,000× less memory than the expanded array — a huge win on embedded hardware.
_____________
> Option A: Alias Method (Vose's Algorithm)

This is the "fairest coin-flip table" approach — O(1) per pick with O(n) space.

Core Idea
Transform the weight distribution into a uniform table where each slot has exactly two candidates and one coin flip decides between them.

Example: w = [1, 3, 2], total = 6
We want 3 equal slots (n slots, each holding total/n = 2 units of weight)

Step 1: Normalize — each item's "fair share" is total/n = 2
  Index 0: 1/2 = 0.5  (underfull)
  Index 1: 3/2 = 1.5  (overfull)
  Index 2: 2/2 = 1.0  (exact)

Step 2: Build the table — take from overfull, give to underfull
  Slot 0: [0, 1]  — index 0 gets its 0.5, index 1 fills the remaining 0.5
  Slot 1: [1, 1]  — index 1 uses its leftover 1.0
  Slot 2: [2, 2]  — index 2 is exactly 1.0

How picking works:

  pickIndex():
    slot = random.randint(0, n-1)       # pick a random slot
    coin = random.random()              # flip a coin [0, 1)
    if coin < probability[slot]:
        return primary[slot]            # the slot's main item
    else:
        return alias[slot]              # the slot's "filler" item

Two random numbers, two array lookups → always O(1).
