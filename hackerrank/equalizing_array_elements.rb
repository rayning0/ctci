#!/bin/ruby

require 'json'
require 'stringio'

# Complete the 'minOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER threshold
#  3. INTEGER d

def minOperations(arr, threshold, d)
    ops = 0
    fr = freq(arr)
    max_equals = fr.values.sort_by{|k,v| k}.last[0]
    return 0 if max_equals >= threshold

    while max_equals < threshold
        ops += 1
        arr.size.times do |i|
            arr[i] /= d
            num = arr[i]
            fr[num] ? fr[num] = [fr[num][0] + 1, fr[num][1] + ops] : fr[num] = [1, ops]
            return fr[num][1] if fr[num][0] >= threshold
        end
    end
    ops
end

def freq(a)
    fr = {}
    a.each do |num|
        fr[num] ? fr[num][0] += 1 : fr[num] = [1, 0]
    end
    fr
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')
