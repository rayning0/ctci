# @param {String} paragraph
# @param {String[]} banned
# @return {String}
def most_common_word(paragraph, banned)
    freq = Hash.new(0)
    mostfreqword = ''
    maxfreq = 0
    paragraph = paragraph.downcase.gsub(/[!?',;.]/, ' ')
    paragraph.split.each do |word|
        freq[word] += 1
    end

    freq.each do |word, f|
        next if banned.include?(word)
        if f > maxfreq
            maxfreq = f
            mostfreqword = word
        end
    end

    mostfreqword
end
