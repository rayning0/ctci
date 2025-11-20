# https://leetcode.com/problems/time-based-key-value-store/description/?envType=problem-list-v2&envId=plakya4j
# Key point: "All the timestamps of set are strictly increasing"!
# Thus they're ALREADY sorted as we insert more entries with set().
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
# Since "All the timestamps of set are strictly increasing"!
# As we set new timestamps for same key, they're ALREADY sorted.
# {key => [[ts1, val1], [ts2 , val2], ...]}
  def set(key, value, timestamp)
    if @hash[key]
      @hash[key] << [timestamp, value]
    else
      @hash[key] = [[timestamp, value]]
    end
  end

# Time: O(log n)
# get(String key, int timestamp) most recent value of key if set() was
# previously called on it and most recent timestamp for that key (prev_timestamp <= timestamp).
# If no values for key, return ''
  def get(key, timestamp)
    return '' if !@hash[key]

    entries = @hash[key] # [[ts1, val1], [ts2 , val2], ...]
    closest = closest_entry(entries, timestamp)

    closest ? closest[1] : ''
  end

  # Since entries already sorted by timestamp, we may use binary search.
  # Find closest entry with timestamp <= target.
  # entries = [[ts1, val1], [ts2 , val2], ...]
  def closest_entry(entries, timestamp)
    # binary search
    l, r = 0, entries.size - 1
    mid = 0
    closest_entry = nil

    while l <= r
      mid = (l + r) / 2

      if entries[mid][0] > timestamp # no entries with later timestamp could be solution
        r = mid - 1
      elsif entries[mid][0] <= timestamp
        closest_entry = entries[mid]
        l = mid + 1
      end
    end

    closest_entry
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

  it '#closest_entry' do
    time_map = TimeMap.new
    entries = [[1, 'ray'], [4, 'gan'], [6, 'man']]
    expect(time_map.closest_entry(entries, 0)).to eq nil
    expect(time_map.closest_entry(entries, 1)).to eq [1, 'ray']
    expect(time_map.closest_entry(entries, 2)).to eq [1, 'ray']
    expect(time_map.closest_entry(entries, 3)).to eq [1, 'ray']
    expect(time_map.closest_entry(entries, 4)).to eq [4, 'gan']
    expect(time_map.closest_entry(entries, 5)).to eq [4, 'gan']
    expect(time_map.closest_entry(entries, 6)).to eq [6, 'man']
    expect(time_map.closest_entry(entries, 10)).to eq [6, 'man']
  end
end
