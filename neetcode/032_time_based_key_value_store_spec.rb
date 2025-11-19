# https://leetcode.com/problems/time-based-key-value-store/description/?envType=problem-list-v2&envId=plakya4j

# Use binary search
# Space: O(m * n), m = total keys, n = # of vals linked to a key
class TimeMap
  def initialize()
    @hash = {}
  end

=begin
  :type key: String
  :type value: String
  :type timestamp: Integer
  :rtype: Void
=end

# Time: O(1)
# As you set new timestamps for same key, must keep them sorted! Maybe use maxheap?
# {key => {ts1 => val1, ts2 => val2, ts3 => val3, ...}}
  def set(key, value, timestamp)
    if @hash[key]
      @hash[key][timestamp] = value
    else
      @hash[key] = {timestamp => value}
    end
  end

# Time: O(log n)
# get(String key, int timestamp) Return most recent value of key if set() was
# previously called on it and most recent timestamp for that key (prev_timestamp <= timestamp).
# If no values for key, return ''
  def get(key, timestamp)
    return '' if !@hash.key?(key)

    timestamps = @hash[key].keys.sort # This uses O(n log n) and violates O(log n) requirement!
    closest_ts = closest_search(timestamps, timestamp)

    closest_ts ? @hash[key][closest_ts] : ''
  end

  # find closest timestamp <= target
  def closest_search(nums, target)
    # handle out of bounds timestamps
    return nums.last if target > nums.last
    return nil if target < nums.first

    # binary search
    l, r = 0, nums.size - 1
    mid = 0
    while l <= r
      mid = (l + r) / 2

      if nums[mid] > target
        r -= 1
      elsif nums[mid] < target
        l += 1
      elsif nums[mid] == target
        return target
      end
    end

    # can't find exact target, so give closest timestamp < target
    next_val = nums[mid + 1]
    if next_val && next_val < target
      next_val
    else
      nums[mid - 1]
    end
  end
end

describe '#TimeMap class' do
  it 'test LeetCode example' do
    time_map = TimeMap.new
    time_map.set("foo", "bar", 1)  # store key "foo", value "bar", timestamp = 1.
    expect(time_map.get("foo", 1)).to eq 'bar'
    expect(time_map.get("foo", 3)).to eq 'bar' # since no value of foo at timestamp 3 and timestamp 2, only value is at timestamp 1 of "bar".
    time_map.set("foo", "bar2", 4) # store key "foo", value "bar2", timestamp = 4.
    expect(time_map.get("foo", 4)).to eq 'bar2'
    expect(time_map.get("foo", 5)).to eq 'bar2'
    expect(time_map.get("foo", 0)).to eq ''
  end

  it 'test NeetCode example' do
    time_map = TimeMap.new
    time_map.set("alice", "happy", 1)
    expect(time_map.get("alice", 1)).to eq 'happy'
    expect(time_map.get("alice", 2)).to eq 'happy'
    time_map.set("alice", "sad", 3)
    expect(time_map.get("alice", 3)).to eq 'sad'
  end

  it '#closest_search' do
    time_map = TimeMap.new
    nums = [1, 4, 6]
    expect(time_map.closest_search(nums, 0)).to eq nil
    expect(time_map.closest_search(nums, 1)).to eq 1
    expect(time_map.closest_search(nums, 2)).to eq 1
    expect(time_map.closest_search(nums, 3)).to eq 1
    expect(time_map.closest_search(nums, 4)).to eq 4
    expect(time_map.closest_search(nums, 5)).to eq 4
    expect(time_map.closest_search(nums, 6)).to eq 6
    expect(time_map.closest_search(nums, 10)).to eq 6
  end
end
