# https://leetcode.com/problems/k-closest-points-to-origin/
# https://www.educative.io/courses/grokking-the-coding-interview/3YxNVYwNR5p
# https://medium.com/basecs/learning-to-love-heaps-cef2b273a238
# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/tutorial/
# https://www.youtube.com/watch?v=t0Cq6tVNRBA
# Runtime: 220 ms, faster than 100.00% of Ruby online submissions for K Closest Points to Origin.
# Memory Usage: 12.1 MB, less than 100.00% of Ruby online submissions for K Closest Points to Origin.

# O(n log n)
def k_closest(points, k)
  points.sort_by{|x, y| x*x + y*y}.first(k)
end

# http://kanwei.github.io/algorithms/classes/Containers/MinHeap.html
require 'algorithms'
include Containers

# O(n log n + k log k) = O(n log n)
def k_closest2(points, k)
  heap = MinHeap.new
  points.each do |x, y|
    d = x*x + y*y
    heap.push(d, [x, y])
  end
  ans = []
  k.times do
    ans << heap.pop
  end
  ans
end

describe '#k_closest' do
  it 'finds k closest points to origin (0,0)' do
    expect(k_closest([[0,1],[1,0]], 2)).to eq [[0,1], [1,0]]
    expect(k_closest([[1,3],[-2,2]], 1)).to eq [[-2,2]]

    now = Time.now
    expect(k_closest([[3,3],[5,-1],[-2,4]], 2)).to eq [[3,3],[-2,4]]
    puts Time.now - now
    # 1.2e-05 secs

    now = Time.now
    expect(k_closest2([[3,3],[5,-1],[-2,4]], 2)).to eq [[3,3],[-2,4]]
    puts Time.now - now
    # 8.0e-05 secs (heap is slower)
  end
end
