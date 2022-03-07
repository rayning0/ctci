// https://leetcode.com/problems/maximum-depth-of-binary-tree/
// https://leetcode.com/submissions/detail/654945067/
// Runtime: 96 ms, faster than 54.45% of JavaScript online submissions for Maximum Depth of Binary Tree.
// Memory Usage: 46 MB, less than 7.86% of JavaScript online submissions for Maximum Depth of Binary Tree.
// Time to write code: 48 secs. (Original time: 26 min)
// 3 companies asking this: LinkedIn, Google, Amazon

// Time complexity: we visit each node exactly once = O(n)
// Space complexity: in the worst case, the tree is completely unbalanced,
// e.g. each node has only left child node, the recursion call would occur N times
// (the height of the tree), therefore storage to keep the call stack would be O(n).
// But in best case (the tree is completely balanced), the height of the tree would be log(n).
// Therefore, the space complexity (with balanced tree) = O(log n)

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

// Use Depth-First Search + Recursion:
let maxDepth = function(root) {
    // console.log(`val: ${root?.val}, L: ${root?.left}, R: ${root?.right}`)

    if (root === null) return 0
    // if (root.left === null || root.right === null) return 1 will NOT work,
    // since for example of [1,null,2], it exits tree before going down to level 2

    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right))
}

For input [3,9,20,null,null,15,7], output:

val: 3, L: [object Object], R: [object Object]
val: 9, L: null, R: null
val: undefined, L: undefined, R: undefined
val: undefined, L: undefined, R: undefined
val: 20, L: [object Object], R: [object Object]
val: 15, L: null, R: null
val: undefined, L: undefined, R: undefined
val: undefined, L: undefined, R: undefined
val: 7, L: null, R: null
val: undefined, L: undefined, R: undefined
val: undefined, L: undefined, R: undefined
_____________
// Approach #2: Tail Recursion + BFS

// Tail recursion: https://www.interviewkickstart.com/learn/tail-recursion
// https://www.geeksforgeeks.org/tail-recursion/
// https://stackoverflow.com/a/37010/2175188

// One might have noticed that the above recursion solution is probably not the most optimal one in terms of the space complexity, and in the extreme case the overhead of call stack might even lead to stack overflow.

// To address the issue, one can tweak the solution a bit to make it tail recursion, which is a specific form of recursion where the recursive call is the last action in the function.

// The benefit of having tail recursion, is that for certain programming languages (e.g. C++) the compiler could optimize the memory allocation of call stack by reusing the same space for every recursive call, rather than creating the space for each one. As a result, one could obtain the constant space complexity \mathcal{O}(1)O(1) for the overhead of the recursive calls.

// Here is a sample C++ solution. Note that the optimization of tail recursion is not supported by Python or Java.

class Solution {

  private:
    // The queue that contains the next nodes to visit,
    //   along with the level/depth that each node is located.
    queue<pair<TreeNode*, int>> next_items;
    int max_depth = 0;

    /**
     * A tail recursion function to calculate the max depth
     *   of the binary tree.
     */
    int next_maxDepth() {

      if (next_items.size() == 0) {
        return max_depth;
      }

      auto next_item = next_items.front();
      next_items.pop();

      auto next_node = next_item.first;
      auto next_level = next_item.second + 1;

      max_depth = max(max_depth, next_level);

      // Add the nodes to visit in the following recursive calls.
      if (next_node->left != NULL) {
        next_items.push(make_pair(next_node->left, next_level));
      }
      if (next_node->right != NULL) {
        next_items.push(make_pair(next_node->right, next_level));
      }

      // The last action should be the ONLY recursive call
      //   in the tail-recursion function.
      return next_maxDepth();
    }

  public:
    int maxDepth(TreeNode* root) {
      if (root == NULL) return 0;

      // clear the previous queue.
      std::queue<pair<TreeNode*, int>> empty;
      std::swap(next_items, empty);
      max_depth = 0;

      // push the root node into the queue to kick off the next visit.
      next_items.push(make_pair(root, 0));

      return next_maxDepth();
    }
};
