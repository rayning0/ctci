def calculate_time(keyboard, word)
    hash = {}
    keyboard.split('').each_with_index do |char, i|
        hash[char] = i
    end
    start = 0
    time = 0

    word.each_char do |char|
        time += (hash[char] - start).abs
        start = hash[char]
    end
    time
end
