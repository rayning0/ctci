# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Runtime: 116 ms, faster than 57.14% of Ruby online submissions for Number of Equivalent Domino Pairs.
# Memory Usage: 11.5 MB, less than 100.00% of Ruby online submissions for Number of Equivalent Domino Pairs.

# Time complexity: O(n). Space complexity: O(n).
def domino_pairs(dominoes)
  freq = Hash.new(0)
  pairs = 0

  dominoes.each do |domino|
    if domino[1] < domino[0]
      freq[[domino[1], domino[0]]] += 1
    else
      freq[domino] += 1
    end
  end
  # puts "freq: #{freq}"

  freq.keys.each do |domino|
    if freq[domino] > 1
      pairs += nChoose2(freq[domino])
      # puts "domino: #{domino}, freq[domino]: #{freq[domino]}, nChoose2: #{nChoose2(freq[domino])}"
    end
  end

  # puts "pairs: #{pairs}\n\n"
  pairs
end

# Algebra: "n choose 2" = # of combinations of n, chosen 2 at a time
# https://www.mathwords.com/c/combination_formula.htm
# http://reddit.com/r/learnmath/comments/3bg21t/what_exactly_is_n_choose_2_in_probability/
# C(n, 2) = n!/(2!(n - 2)!) = n (n - 1) / 2
def nChoose2(n)
  n * (n - 1) / 2
end

describe "#domino_pairs" do
  it 'finds # of equivalent domino pairs' do
    expect(domino_pairs([[1,2],[2,1],[3,4],[5,6]])).to eq 1
    expect(domino_pairs([[1,2],[1,2],[1,1],[1,2],[2,2]])).to eq 3
    expect(domino_pairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]])).to eq 4
  end
end

# freq: {[1, 2]=>2, [3, 4]=>1, [5, 6]=>1}
# domino: [1, 2], freq[domino]: 2, nChoose2: 1
# pairs: 1

# freq: {[1, 2]=>3, [1, 1]=>1, [2, 2]=>1}
# domino: [1, 2], freq[domino]: 3, nChoose2: 3
# pairs: 3

# freq: {[1, 1]=>3, [2, 2]=>1, [1, 2]=>2}
# domino: [1, 1], freq[domino]: 3, nChoose2: 3
# domino: [1, 2], freq[domino]: 2, nChoose2: 1
# pairs: 4
