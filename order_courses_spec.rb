# Given college courses, each with array of prereqs, return possible order of
# courses to take, so you always take prereqs before each related course

# Depth-first search algorithm with stack

def order(hash)
  ans, stack = [], []

  hash.each do |id, pre|
    if pre == []
      ans << id.to_s if !ans.include?(id.to_s)
      next
    end

    stack << id.to_s

    while !stack.empty?
      top = stack.last
      if !ans.include?(top) && hash[top.to_sym] == []
        ans << stack.pop
      end

      hash[top.to_sym].each do |prereq|
        if !ans.include?(prereq) && !stack.include?(prereq) # not visited
          stack << prereq
          if !ans.include?(top) && prereq == []
            ans << top
          end
        end
      end

      hash[top.to_sym] = [] # marks value of top as visited
    end
  end

  ans
end

describe '#order' do
  it 'returns articles in proper order, first showing prereqs' do
    expect(order({'A': [], 'B': [], 'C': []})).to eq ['A', 'B', 'C']
    expect(order({'A': ['B'], 'B': [], 'C': []})).to eq ['B', 'A', 'C']
    expect(order({'A': ['B', 'C'], 'B': [], 'C': []})).to eq ['C', 'B', 'A']
    expect(order({'A': [], 'B': ['C', 'D'], 'C': ['D'], 'D': []})).to eq ['A', 'D', 'C', 'B']
    expect(order({'A': ['E'], 'B': ['C', 'D', 'E'], 'C': ['D', 'E'], 'D': [], 'E': []})).to eq ['E', 'A', 'D', 'C', 'B']
  end
end
