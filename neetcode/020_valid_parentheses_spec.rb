# https://leetcode.com/problems/valid-parentheses/?envType=problem-list-v2&envId=plakya4j
# Use stack
# 1. If char is left paren, add to stack.
# 2. If char is right paren ')' and:
#   a. Stack is empty [], return false
#   b. Top of stack is wrong left paren '{', return false
#   c. Top of stack is matching left paren '(', pop off top of stack.

# Time: O(n), Space: O(n)
def is_valid(s)
  stack = []
  paren = {')' => '(', ']' => '[', '}' => '{'}

  s.each_char do |c|
    # if char is right paren
    if paren[c]
      return false if stack == [] || stack.last != paren[c]
      stack.pop if stack.last == paren[c]
    else
      stack << c
    end
  end

  stack.size == 0 ? true : false
end

describe 'valid parentheses' do
  it 'determine if input string of parentheses is valid' do
    expect(is_valid("[")).to eq false
    expect(is_valid("()")).to eq true
    expect(is_valid("()[]{}")).to eq true
    expect(is_valid("(]")).to eq false
    expect(is_valid("([{}])")).to eq true
    expect(is_valid("([)]")).to eq false
  end
end
