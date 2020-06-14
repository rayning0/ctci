def mutateTheArray(n, a)
    b = []
    a.size.times do |i|
        first = i == 0 ? 0 : a[i - 1]
        last = i == a.size - 1 ? 0 : a[i + 1]
        b[i] = first + a[i] + last
    end
    b
end

def countTinyPairs(a, b, k)
    ans = 0
    a.size.times do |i|
        ans += 1 if (a[i].to_s + b[a.size - 1 - i].to_s).to_i < k
    end
    ans
end

def meanGroups(a)
    h = {}
    a.each_with_index do |arr, i|
        mean = arr.inject(&:+).to_f / arr.size
        h[mean] ? h[mean] << i : h[mean] = [i]
    end
    h.values
end

def alternatingSort(a)
    return true if a.size == 1
    alt_i = 0
    b = [a[alt_i]]
    sign = -1
    (a.size - 1).downto(1).each do |i|
        sign *= -1
        alt_i += sign * i
        b << a[alt_i]
    end

    if b == b.sort
        (0..b.size - 2).each do |i|
            return false if b[i] == b[i + 1]
        end
        true
    else
        false
    end
end


def mergeStrings(s1, s2)
    ans = ''
    i, j = 0, 0
    s1, s2 = s2, s1 if s1.size > s2.size
    freq1, freq2 = freq_hash(s1), freq_hash(s2)
    while j < s2.size
        char1, char2 = s1[i], s2[j]
        if char1.nil?
            ans += s2[j..-1]
            break
        elsif char2.nil?
            ans += s1[i..-1]
            break
        end

        if freq1[char1] < freq2[char2]
            ans += char1
            i += 1
        elsif freq1[char1] > freq2[char2]
            ans += char2
            j += 1
        elsif char1 < char2
            ans += char1
            i += 1
        elsif char1 > char2
            ans += char2
            j += 1
        else
            ans += char1
            i += 1
            j += 1
        end
    end
    ans += s1[i..-1] if i < s1.size
    ans
end

def freq_hash(str)
  f = {}
  str.each_char do |char|
    f[char] ? f[char] += 1 : f[char] = 1
  end
  f
end

# Given integer array, return sum of every array[i] concatenated with array[j].
# For example: arr[1,2,3] would give -> 11+12+13+21+22+23+31+32+33

#  For a = [10,2], the output should be concatentationSum(a) = 1344
#  - a[0] + a[0] = 10 + 10 = 1010
#  - a[0] + a[1] = 10 + 2 = 102
#  - a[1] + a[0] = 2 + 10 = 210
#  - a[1] + a[1] = 2 + 2 = 22
#  So the sum is equal to 1010 + 102 + 210 + 22 = 1344

def concatenations_sum(a)
  ans = 0
  a.size.times do |i|
    a.size.times do |j|
      ans += (a[i].to_s + a[j].to_s).to_i
    end
  end
  ans
end

# p concatenations_sum([10, 2]) is 1344

#----------------
# 28/30 tests passed. Execution time limit exceeded on test 29: Program exceeded the execution time limit. Make sure that it completes execution in a few seconds for any possible input.
def hashMap(queryType, query)
    h = {}
    sum = 0
    query.size.times do |i|
        qt, q = queryType[i], query[i]
        case qt
        when 'insert'
            key, val = q
            h[key] = val
        when 'addToValue'
            h = add_to_value(h, q[0])
        when 'addToKey'
            h = add_to_key(h, q[0])
        when 'get'
            sum += h[q[0]]
        end
    end
    sum
end

def add_to_value(h, num)
    h.each do |key, val|
        h[key] += num
    end
    h
end

def add_to_key(h, num)
    h2 = {}
    h.each do |key, val|
        h2[key + num] = val
    end
    h2
end
#----------------
