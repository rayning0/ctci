# https://leetcode.com/problems/relative-sort-array/
# Runtime: 36 ms, faster than 66.67% of Ruby online submissions for Relative Sort Array.
# Memory Usage: 9.4 MB, less than 100.00% of Ruby online submissions for Relative Sort Array.
def relative_sort_array(arr1, arr2)
    output = []
    arr1.sort!
    f1, f2 = {}, {}
    arr1.each do |num|
        f1[num] ? f1[num] += 1 : f1[num] = 1
    end
    arr2.each do |num|
        f2[num] ? f2[num] += 1 : f2[num] = 1
    end

    f2.each do |num, freq|
        if f1[num]
            f1[num].times do |i|
              output << num
              f1.delete(num)
            end
        end
    end

    f1.each do |num, freq|
        freq.times do |i|
            output << num
        end
    end

    output
end
