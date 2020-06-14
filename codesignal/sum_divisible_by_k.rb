def sum_divisible_by_k(a, k)
    ways = 0
    freq = Array.new(k, 0)

    a.each do |num|
        rem = num % k
        if rem != 0
            ways += freq[k - rem]
        else
            ways += freq[0]
        end
        freq[rem] += 1
    end

    ways
end

p s([1, 2, 3, 4, 5], 3)
