def tsort(arr)
  arr.sort_by{ |word, num| num }
end

describe '#tsort' do
  it 'sorts tuples by 2nd value' do
    expect(tsort([['for', 24], ['Geeks', 8], ['Geeks', 30]])).to eq([['Geeks', 8], ['for', 24], ['Geeks', 30]])
    expect(tsort([['452', 10], ['256', 5], ['100', 20], ['135', 15]])).to eq [['256', 5], ['452', 10], ['135', 15], ['100', 20]]
  end
end

hash = {
         'a': 'apple',
         'b': 'dog',
         'c': {'d': 'dog'},
         'e': 'dog',
         'f': {'g': {'h': 'dog'}}
       }

# Given hash and value, give list of all keys with that value. If nested, keys should be separated by a dot.
def hashkeys(hash, val, ans = [], keylist = nil)
  hash.each do |k, v|
    if v.is_a?(Hash)
      keylist = addkey(k, keylist)
      hashkeys(v, val, ans, keylist)
      keylist = nil
    elsif v == val
      keylist = addkey(k, keylist)
    end
    if keylist
      ans << keylist
      keylist = nil
    end
  end

  ans
end

def addkey(k, keylist)
  if keylist.nil?
    k.to_s
  else
    keylist + '.' + k.to_s
  end
end

describe '#hashkeys' do
  it 'given hash and value, gives list of all keys with that value' do
    expect(hashkeys(hash, 'dog')).to eq ['b', 'c.d', 'e', 'f.g.h']
  end
end

# Given sorted list of Unix epoch time deliveries for customers, return UUIDs for customers with 3+ deliveries in any 30 day period.
def busy_customers(deliveries)
  secs_in_month = 60 * 60 * 24 * 30
  hash = {} # {id: [time difference, # of deliveries]}
  ans = []
  deliveries.each do |id, time|
    if hash[id]
      last_time, delivery_num = hash[id]
      if time - last_time < secs_in_month
        delivery_num += 1
        hash[id][1] = delivery_num
        next
      end
    end

    hash[id] = [time, 1]
  end

  hash.each do |id, arr|
    ans << id if arr[1] >= 3
  end

  ans
end

describe '#busy_customers' do
  it 'Given list of deliveries (at Unix epoch times), returns customer IDs with 3+ deliveries in any 30 day period' do
    deliveries = [
      ['1', 1586182280],
      ['2', 1586227080],
      ['1', 1590460680],
      ['1', 1591670280],
      ['2', 1591905480],
      ['3', 1592005480],
      ['1', 1592707080],
      ['3', 1592805480],
      ['2', 1592907080],
      ['3', 1594521480],
    ]
    expect(busy_customers(deliveries)).to eq ['1', '3']
  end
end

# XOR: a ^ a ^ b = a ^ b ^ a = b ^ a ^ a = b
# a ^ a ^ a = a
def good_tuples(nums)
  count = 0
  (0..nums.size - 3).each do |i|
    first, second, third = nums[i], nums[i + 1], nums[i + 2]
    next if 3 * first == first + second + third
    count += 1 if [first, second, third].include?(first ^ second ^ third)

    # next if nums[i] == nums[i + 1] && nums[i + 1] == nums[i + 2]
    # next if nums[i] != nums[i + 1] && nums[i + 1] != nums[i + 2] && nums[i] != nums[i + 2]
  end

  count
end

describe '#good_tuples' do
  it 'returns # of good tuples, or # of consecutive triplets with exactly 2 duplicate numbers' do
    expect(good_tuples([4,4,6,4,2,2,2,3])).to eq 4
    # [446], [464], [422], [223]
  end
end

# https://leetcode.com/discuss/interview-question/506181/Postmates-or-OA-2020-or-Close-Strings
def close_strings(str1, str2)
  freq1, freq2 = freq_hash(str1), freq_hash(str2)
  freq1 = freq1.sort_by {|char, freq| freq}
  freq2 = freq2.sort_by {|char, freq| freq}
  freq1.size.times do |i|
    return false if freq1[i][1] != freq2[i][1]
  end

  true
end

def freq_hash(str)
  f = {}
  str.each_char do |char|
    f[char] ? f[char] += 1 : f[char] = 1
  end
  f
end

describe '#close_strings' do
  it 'returns T or F, if we may convert one string to another' do
    expect(close_strings("abbzccc", "babzzcz")).to eq true
    expect(close_strings("abcbdb", "bbbcca")).to eq false
    expect(close_strings("abbbzcc", "babzzcz")).to eq true
    expect(close_strings("abbbzcf", "babzzcz")).to eq false
    expect(close_strings("abbzzca", "babzzcz")).to eq false
  end
end

# Given time window (start, finish) in which courier works and array of start/finish times of deliveries.
# Find max number of deliveries courier can make, with no overlapping times.

# Answer: First sort intervals by finish time value. Then insert first interval into answer and continue considering each interval in turn: If current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to answer.

# Time complexity: n log n, from sort
def no_overlap(time_window, deliveries)
  ans = []
  earliest, latest = time_window
  deliveries.sort_by!{ |start, finish| finish }
  deliveries.each do |start, finish|
    next if start < earliest || finish > latest
    if ans.empty?
      ans = [[start, finish]]
    elsif ans.last[1] < start
      ans << [start, finish]
    end
  end

  ans
  # ans.size
end

describe '#no_overlap' do
  it 'finds max # of deliveries with no overlapping times' do
    expect(no_overlap([1, 50], [[1, 5], [10, 25], [17, 21], [30, 60], [11, 16]])).to eq [[1,5], [11,16], [17,21]]
    expect(no_overlap([2, 50], [[1, 5], [10, 25], [17, 21], [30, 60], [11, 16]])).to eq [[11,16], [17,21]]
    expect(no_overlap([1, 50], [[1, 12], [10, 25], [17, 21], [14, 16], [30, 60], [11, 13], [5, 9]])).to eq [[5, 9], [11, 13], [14, 16], [17, 21]]
    expect(no_overlap([1, 50], [[1, 5], [10, 25], [17, 21], [30, 50], [11, 16]])).to eq [[1,5], [11,16], [17,21], [30, 50]]
  end
end
