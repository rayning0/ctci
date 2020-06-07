def eval(exp)
  stack = []
  num, op = '', ''

  exp.each_char do |char|
    # next if [' ', ','].include?(char)
    if ['[', '&', '|', '!', '0', '1'].include?(char)
      stack << char
    elsif char == ']'
      if stack[-2] == '['
        break
      elsif stack[-2] == '!'
        num = stack.pop
        stack.pop
        stack.pop
        stack << simple_eval('!', num)
      else
        num2 = stack.pop
        num1 = stack.pop
        op = stack.pop
        stack.pop
        return 'Error: First value is not logic operator' if op == '['
        stack << simple_eval(op, num1, num2)
      end
    end
  end

  stack.pop
end

def to_bool(num)
  num.to_i == 1 ? true : false
end

def to_string(bool)
  bool ? '1' : '0'
end

def simple_eval(op, num1, num2 = nil)
  case op
  when '&'
    to_string(to_bool(num1) && to_bool(num2))
  when '|'
    to_string(to_bool(num1) || to_bool(num2))
  when '!'
    to_string(!to_bool(num1))
  else
    'Error: First value is not logic operator'
  end
end

describe '#eval' do
  it 'evaluates expression with no nesting' do
    expect(eval('[&, 1, 0]')).to eq '0'
    expect(eval('[&, 0, 0]')).to eq '0'
    expect(eval('[&, 1, 1]')).to eq '1'
    expect(eval('[!, 1]')).to eq '0'
    expect(eval('[!, 0]')).to eq '1'
    expect(eval('[|, 1, 0]')).to eq '1'
    expect(eval('[|, 1, 1]')).to eq '1'
    expect(eval('[|, 0, 0]')).to eq '0'
    expect(eval('[1, 0]')).to eq 'Error: First value is not logic operator'
  end

  it 'evaluates 1 level of nesting' do
    expect(eval('[&, 1, [!, 0]]')).to eq '1'
    expect(eval('[|, [&, 1, [!, 0]], 0]')).to eq '1'
  end

  it 'evaluates 2 levels of nesting' do
    expect(eval('[|, [&, 1, [!, 0]], [!, [|, [|, 1, 0], [!, 1]]]]')).to eq '1'

    # OUTPUT:
    # ["["]
    # ["[", "|"]
    # ["[", "|", "["]
    # ["[", "|", "[", "&"]
    # ["[", "|", "[", "&", "1"]
    # ["[", "|", "[", "&", "1", "["]
    # ["[", "|", "[", "&", "1", "[", "!"]
    # ["[", "|", "[", "&", "1", "[", "!", "0"]
    # ["[", "|", "[", "&", "1", "1"]
    # ["[", "|", "1"]
    # ["[", "|", "1", "["]
    # ["[", "|", "1", "[", "!"]
    # ["[", "|", "1", "[", "!", "["]
    # ["[", "|", "1", "[", "!", "[", "|"]
    # ["[", "|", "1", "[", "!", "[", "|", "["]
    # ["[", "|", "1", "[", "!", "[", "|", "[", "|"]
    # ["[", "|", "1", "[", "!", "[", "|", "[", "|", "1"]
    # ["[", "|", "1", "[", "!", "[", "|", "[", "|", "1", "0"]
    # ["[", "|", "1", "[", "!", "[", "|", "1"]
    # ["[", "|", "1", "[", "!", "[", "|", "1", "["]
    # ["[", "|", "1", "[", "!", "[", "|", "1", "[", "!"]
    # ["[", "|", "1", "[", "!", "[", "|", "1", "[", "!", "1"]
    # ["[", "|", "1", "[", "!", "[", "|", "1", "0"]
    # ["[", "|", "1", "[", "!", "1"]
    # ["[", "|", "1", "0"]
    # ["1"]
  end
end
