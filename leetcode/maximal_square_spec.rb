def maximal_square(arr)
  max_square_size, square_size = 0, 0

  arr.size.times do |row|
    arr[0].size.times do |col|
      square_size = scan_square(row, col, arr)
      max_square_size = [max_square_size, square_size].max
    end
  end

  max_square_size
end

def scan_square(row, col, arr)
  height = arr.size
  width = arr[0].size
  side = 1
  square_size = 0

  while col + side - 1 < width && row + side - 1 < height do
    (row..row + side - 1).each do |r|
      (col..col + side - 1).each do |c|
        return square_size * square_size if arr[r][c] == '0'
      end
    end
    square_size += 1

    side += 1
  end

  square_size * square_size
end

describe "#maximal_square" do
  # it '' do
  #   arr = [
  #     ["1","0","1","1","1"],
  #     ["1","0","1","1","1"],
  #     ["1","1","1","1","1"],
  #     ["1","1","1","1","1"]
  #   ]
  #   expect(scan_square(2, 0, arr)).to eq 4
  # end
  it "returns biggest square with only 1's" do
    expect(maximal_square([
      ["0","0"],
      ["0","0"],
    ])).to eq 0
    expect(maximal_square([
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ])).to eq 4
  end
end
