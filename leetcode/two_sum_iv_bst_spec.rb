# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Runtime: 52 ms, faster than 100.00% of Ruby online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 10.2 MB, less than 100.00% of Ruby online submissions for Two Sum IV - Input is a BST.

# Time complexity: O(n). Space complexity: O(n). n = # of nodes.
class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

root = TreeNode.new(5)
root.left = TreeNode.new(3)
root.left.left = TreeNode.new(2)
root.left.right = TreeNode.new(4)
root.right = TreeNode.new(6)
root.right.right = TreeNode.new(7)

# @param {TreeNode} root
# @param {Integer} k
# @return {Boolean}
def find_target(root, k)
  @k, @hash = k, {}

  return true if find_diff(root)
  false
end

def find_diff(root)
    return if root.nil?
    diff = @k - root.val
    return true if @hash[root.val]
    @hash[diff] = true

    find_diff(root.left) || find_diff(root.right)
end

describe '#find_target' do
  it 'returns if there exists 2 elements in binary search tree so sum == target' do
    expect(find_target(root, 9)).to eq true
    expect(find_target(root, 28)).to eq false
    expect(find_target(root, 12)).to eq true
  end
end
