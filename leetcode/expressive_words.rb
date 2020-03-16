# https://leetcode.com/problems/expressive-words/
def expressive_words(s, words)
    numwords = 0
    words.each do |word|
        i, j = 0, 0
        ok = false
        while i < s.size do
            if s[i] && word[j].nil?
                ok = false
                break
            end
            scommon, word_common = 0, 0
            sindex, jindex = i, j
            while s[sindex] == word[j] do
                scommon += 1
                sindex += 1
            end
            while s[i] == word[jindex] do
                word_common += 1
                jindex += 1
            end

            if scommon == 0 || word_common > scommon
                ok = false
                break
            end

            if scommon == word_common || scommon >= 3
                i += scommon
                j += word_common
                ok = true
            end

            if scommon < 3 && scommon != word_common
                ok = false
                break
            end

            ok = true
        end

        numwords += 1 if ok
    end

    numwords
end
# a
# scommon = 1
# i = 4
# s = "aaabaa"
# word = "ab"

# a
# wcommon = 1
# j = 2

s = "yyrrrrrjaappoooyybbbebbbbriiiiiyyynnnvvwtwwwwwooeeexxxxxkkkkkaaaaauuuu"
words = ["yrrjjappooybbebriiyynvvwtwwoeexkauu","yrjjappooybbebrriyynnvwwttwoeexkaauu","yyrrjapoybbebriiynnvvwwtwoeexkaauu","yyrjappooyybebbrriyynnvwttwwooeexxkkau","yrjaapooybbebrriyynnvvwwttwooexkaau","yyrjjapooyybeebbrriiyynvwwttwoexxkau","yrrjaappoyybbeebbriynnvwwtwooexxkauu","yrrjjaapooybebriynnvvwwttwwooexkaau","yyrrjjappooyybebriiyynvvwttwoeexxkkaau","yrrjaappooybbebrriynvwwtwooeexkau","yyrjjaapooyybebrriiynvvwttwwooeexxkkaau","yyrrjappooyybbebriyynnvwwttwwoeexkkauu","yyrrjjaapoyybbeebriiyynnvwwtwwooexkkaau","yrjjaappooybbeebriiyynnvwwtwwoexkau","yrrjjappoyybbeebbrriiyynnvwttwwooexxkkaauu","yyrrjjapooyybbebbrriyynvwtwoexxkkaauu","yyrrjappoybebrriynvwwttwooeexkkauu","yrrjaappooybbeebriiyynnvvwwttwoexxkauu","yrrjapoybebbrriyynvvwwttwwoexkaau","yyrrjjapoybbeebbrriynnvwwtwwooexkaauu","yyrrjjapooyybbeebbriyynnvwtwwoexkaau","yrjjaapooyybebriynnvwwttwooeexxkkaauu","yyrjjaapooybbebbriiynvvwttwwoexxkkauu","yrjjaapooyybeebbriiyynvvwwttwoeexxkau","yrjjappooyybbebbrriiynvvwtwooeexxkkau","yyrrjjapoyybbebbrriiyynvwwtwwoexxkkaau","yrjjapooyybbeebriyynnvvwwtwoeexkkau","yrjapooyybebriiynnvvwwtwwooeexkauu","yyrjaapoyybbebbrriynnvwtwwoeexkauu","yrrjjappoybeebrriiynvvwwtwwoeexxkkaau","yrrjjapoybbeebrriiyynnvwwttwwoexxkaau","yyrrjaapoybeebrriiyynvwttwwooeexkauu","yyrjapoybbeebbrriyynnvvwwttwwooeexkaauu","yyrjappooybebrriiynvwtwwoeexxkaauu","yrrjjappooybebrriynnvvwttwooexkau","yrjjaapoybbeebbriiynnvvwttwooexkauu","yyrrjapooyybbeebriiyynnvvwtwwoeexxkaauu","yyrjjaappooybeebbrriiyynnvvwwtwwoeexkkau","yrrjappoyybbeebrriiynvvwwtwwoeexxkauu","yrjapooyybeebriiyynvvwttwwooeexxkaauu","yrjjappooyybbebbriiynnvwwtwooeexxkauu","yyrrjjappooybbeebbriyynnvwtwwooexxkkau","yyrrjjaapooybebriiyynvwwtwooeexxkkaauu","yrjjappooyybbeebbriiyynvwwtwwoeexkkau","yrrjjappooybbebrriiynvvwwtwwoexxkkaau","yrjjapooybebbriyynnvvwwttwwooeexxkkaau","yyrjjapoyybebbrriynvvwwttwoexkauu","yyrjappoyybebriiynnvvwttwwoexxkaauu","yyrjaapoybbeebriyynvvwwttwoeexkau","yrjjaappooyybbebbriiynnvvwtwooexxkau","yyrjjaappooyybbebrriiyynvvwttwooexkau","yrjjappoybbeebriyynnvvwwttwwooexxkkaau","yyrrjaapooybbebbriiyynnvwwtwwooexxkkaauu","yrrjaapooybbeebrriynnvvwwtwoeexxkkauu","yrjjaappooyybeebbrriyynnvvwttwwoexxkkauu","yrrjapooyybebriyynnvwwttwooeexkau","yyrjjaapooyybeebrriiynnvvwwttwoeexxkkau","yrjappooybebriyynnvvwttwwooeexkau","yrrjjaappoyybebbrriiyynvwwtwooexxkauu","yrjjappooybeebriynnvwwtwoeexkaauu","yrjaappoybbebbriiynnvwwttwooexxkaau","yyrrjappooyybeebbriiyynvwwttwwoexxkau","yyrjappoyybbeebrriynvwtwoeexkaau","yrrjjaapooybbeebbriyynvwwtwooeexkkaau","yrjapoybebbrriiynvwttwwoeexxkaau","yrjapooybebbrriiynnvwwtwwoexxkaau","yrrjjaappoybeebbriiyynvwwtwooexxkkaauu","yrjappooybeebrriynvwwtwooeexkaauu","yrrjaapooybeebbriiynvvwtwwoexxkkaauu","yyrrjaappooyybebbrriiyynvwwtwwooexxkkau","yyrjaappoybbeebriynnvvwwtwwooeexkaauu","yyrjaappooyybbebbriynvvwwttwwooexkauu","yrjappooybeebbrriiynnvwttwwooexkkau","yrrjjappooyybebbriiyynnvvwttwwoexkkau","yrrjjaapooybeebbriynnvvwwtwooexkaau","yyrjjappoybeebbrriiynnvwtwwoexkaauu","yyrjjaapoybbebbrriiyynnvvwtwwoexkaau","yyrrjjaappoyybbebbriyynvwwtwwooeexkkaau","yrrjjaappooybbebriiyynvvwttwwooexxkau","yyrjjaapoyybebriiynnvwtwwooeexkauu","yrrjjappoyybeebbriiyynnvwttwoexkkau","yrjjappoyybbebbrriynnvvwttwwooeexkkaauu","yyrjappooybeebrriiynnvwwttwwooexxkkaauu","yrrjaappoybbeebrriyynnvvwwtwwooeexxkaauu","yyrjaappooybeebbriiynvwttwoexxkkauu","yyrrjjapooyybbeebbrriyynvwttwwooeexxkkau","yrrjapoybbebbrriiynvwtwwoeexxkaau","yyrrjapoybbeebbriiyynnvvwttwooexkkauu","yyrjaapooyybebbrriiyynnvvwwtwooeexkkauu","yyrrjjaappoybbeebrriyynnvwwtwwoexkkaauu","yyrjappooybbeebrriiyynvwwttwwoexkkau","yyrjaapooyybebbriiyynnvvwwtwoeexkkaau","yyrrjjappoyybbeebbriiyynvwtwooexxkaauu","yrrjjaapoyybbeebriynvvwtwwoexxkaau","yyrrjjapoybbebbrriyynnvwwtwoeexxkkaau","yyrrjapooyybebrriiyynvwttwwooeexxkkauu","yrjappooyybebriiynnvwwtwoeexkkaauu","yrjjaapooyybeebriiynvwtwooexkauu","yyrrjjapoybeebbrriiynnvwttwwoexkaau","yyrrjaappoyybebbrriiyynvwwtwooeexkaau"]

puts expressive_words(s, words)
