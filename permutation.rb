# print all permutations of a string
# https://www.topcoder.com/generating-permutations/
# Also see my past answers: https://github.com/rayning0/codility/blob/master/permutation.rb

# 2 swap algorithm. Faster!
def permutation(str, n = str.length)
  if n == 1
    puts str
  else
    n.times do |i|
      str[i], str[n - 1] = str[n - 1], str[i] # swap str[i] with str[n-1]
      permutation(str, n - 1)
      str[i], str[n - 1] = str[n - 1], str[i]
    end
  end
end

# Decrease and Conquer:
# 1. divide the problem into two parts: a sub-problem of size (n -1) and a single remaining element.
# 2. solve the sub-problem of size (n-1) by a recursive call (or an iterative decreasing process).
# 3. add the remaining individual element back into the sub-problem’s solution.
def permute(a)
  return [a] if a.size < 2
  perms = []
  a.each do |elem|
    permute(a - [elem]).each do |p|
      perms << ([elem] + p)
    end
  end
  perms
end

str = 'dear'

now = Time.now
permutation(str)
puts "#{Time.now - now} secs. Faster algorithm"

now = Time.now
p permute(str.split('')).map(&:join)
puts "#{Time.now - now} secs"

# OUTPUT:

# eard
# aerd
# ared
# raed
# erad
# read
# rade
# arde
# adre
# dare
# rdae
# drae
# erda
# reda
# rdea
# drea
# edra
# dera
# eadr
# aedr
# ader
# daer
# edar
# dear
# 7.7e-05 secs

# ["dear", "dera", "daer", "dare", "drea", "drae", "edar", "edra", "eadr", "eard", "erda", "erad", "ader", "adre", "aedr", "aerd", "arde", "ared", "rdea", "rdae", "reda", "read", "rade", "raed"]
# 0.000109 secs