# https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=plakya4j

# 1. Naive answer: Make freq hash of nums. Make array of [count, num].
# Sort it by count. Take last k elements.
# Time: O(n log n), Space: O(n)

# def top_k_frequent(nums, k)
#   freq = Hash.new(0)
#   nums.each do |num|
#     freq[num] += 1
#   end

#   arr = []
#   freq.each do |num, count|
#     arr << [count, num]
#   end
#   arr.sort! # by default, sorts by first element of each nested array ("count")

#   arr.last(k).map { |num, count| count }
# end

# 2. Better: MaxHeap

# Time: O(n log n), Space: O(n)
# - Build freq hash: O(n)
# - Build MaxHeap with ALL unique elements: O(u log u) = O(n log n) worst case
#   (heap grows to size u = number of unique elements)
# - Pop k times: O(k log u) = O(k log n)
# - Total: O(n) + O(n log n) + O(k log n) = O(n log n)
# Space: O(n) for freq hash + O(n) for heap = O(n)

# require 'algorithms'
# include Containers

# def top_k_frequent(nums, k)
#   freq = Hash.new(0)
#   nums.each do |num|
#     freq[num] += 1
#   end

#   # Step 2: Use MaxHeap to keep only k largest frequencies
#   max_heap = MaxHeap.new
#   freq.each do |num, count|
#     max_heap << [count, num] # it sorts by first element ("count") and makes this root of heap
#   end

#   k.times.map { max_heap.pop[1] }
# end

# 3. Even better: MinHeap with size limit

# Time: O(n log k), Space: O(n)
# - Build freq hash: O(n)
# - Build MinHeap limited to size k: O(n log k)
#   (each push is O(log k) since heap never exceeds size k)
# - Pop k times: O(k log k)
# - Total: O(n) + O(n log k) + O(k log k) = O(n log k) when k < n
# Space: O(n) for freq hash + O(k) for heap = O(n) overall
#   (but heap space is O(k), which is better than O(n) in MaxHeap)

# require 'algorithms'
# include Containers

# def top_k_frequent(nums, k)
#   freq = Hash.new(0)
#   nums.each do |num|
#     freq[num] += 1
#   end

#   min_heap = MinHeap.new
#   freq.each do |num, count|
#     min_heap << [count, num]
#     min_heap.pop if min_heap.size > k # deletes all lower freq nums
#   end

#   k.times.map { min_heap.pop[1] }
# end

# 4. Best! Bucket Sort

# Time: O(n), Space: O(n)
# - Build freq hash: O(n) time, O(u) space where u = unique elements (worst case u = n)
# - Create bucket array: O(n) time, O(n) space (array of size n+1)
# - Populate buckets: O(u) time, O(u) space (each unique element goes into one bucket)
# - Iterate backwards through buckets: O(n) time worst case (iterate through all n+1 buckets)
# - Concatenate and take k: O(k) time worst case
# Total Time: O(n) + O(n) + O(u) + O(n) + O(k) = O(n) since u ≤ n and k ≤ n
# Total Space: O(u) + O(n) + O(k) = O(n) (freq hash + bucket array + answer)
def top_k_frequent(nums, k)
  # freq = Hash.new(0)
  # nums.each do |num|
  #   freq[num] += 1
  # end

  freq = nums.tally
  freq.default = 0

  # Make frequency bucket. Bucket index is "count" from freq hash, # of times each num appears.
  # In each array element, put array with all nums that repeat "count" times.
  # Then loop through bucket backwards, from highest to lowest count.
  # Return first k nums in answer.

  # This format makes each element INDEPENDENT empty array. Don't do Array.new(6, [])!
  bucket = Array.new(nums.length + 1) { [] }
  freq.each do |num, count|
    bucket[count] << num
  end

  ans = []
  bucket.reverse_each do |vals|
    next if vals.empty?
    ans.concat(vals)
    return ans if ans.length >= k
  end
end

describe "#top_k_frequent" do
  it 'returns the k most frequent elements' do
    expect(top_k_frequent([1,1,1,2,2,3], 2)).to eq [1, 2]
    expect(top_k_frequent([1], 1)).to eq [1]
    expect(top_k_frequent([7,7], 1)).to eq [7]
    expect(top_k_frequent([1,2,1,2,1,2,3,1,3,2], 2)).to eq [1, 2]
  end
end
