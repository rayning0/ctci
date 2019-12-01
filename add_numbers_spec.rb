# Add Big Numbers
# QUESTION: Take 2 positive numbers as strings and return their sum.
# Must work for VERY LARGE positive numbers.
# You may not just convert strings to numbers and add them.

# STRATEGY:
# 1. Split string by decimal point ('.') to separate integer from decimal part. Get 2 arrays of characters. One for integer. One for decimals.
# 2. Loop through each character and, based on index in array, multiply its value by the corresponding power of 10.
# 3. Keep a running sum of each.

# Better answer than mine, which does NOT require 'bigdecimal'. It carries the 10s and adds them:
# https://www.geeksforgeeks.org/sum-two-large-numbers/

# Ex: '512.34' + '25.67'

# 512.34 =
# 5 * 10**2 +
# 1 * 10**1 +
# 2 * 10**0 +
# 3 * 10**-1 +
# 4 * 10**-2

# index   exponent
# ________________
# 0         2
# 1         1
# 2         0

# 'bigdecimal' gives us PERFECT PRECISION arithmetic for long decimal numbers:
# https://www.rubyguides.com/2016/07/numbers-in-ruby/
require 'bigdecimal'

def add(num1, num2)
  int1, dec1 = num1.split('.')
  int2, dec2 = num2.split('.')
  sum = 0

  max_length = [int1.length, int2.length, dec1.length, dec2.length].max

  max_length.times do |dec_index|
    int_index = -1 - dec_index
    int1 = '0' + int1 if int1[int_index].nil?
    int2 = '0' + int2 if int2[int_index].nil?
    dec1 += '0' if dec1[dec_index].nil?
    dec2 += '0' if dec2[dec_index].nil?
    puts "int1: #{int1}, int2: #{int2} | dec1: #{dec1}, dec2: #{dec2}"

    sum += (BigDecimal(int1[int_index]) + BigDecimal(int2[int_index])) * 10**dec_index
    puts "dec_index: #{dec_index}, int_index: #{int_index}"
    puts "int_sum: #{sum}"

    sum += (BigDecimal(dec1[dec_index]) + BigDecimal(dec2[dec_index])) * 10**int_index
    puts "int_sum + dec_sum: #{sum}\n\n"
  end
  puts "----------------------"
  sum
end

describe '#add' do
  it 'adds 2 small numbers' do
    expect(add('512.349', '25.67')).to eq 538.019
    expect(add('25.67', '512.349')).to eq 538.019
    expect(add('23423.97655', '0.3668558')).to eq 23424.3434058

    a = '95745735635754675467.4452345234546'
    b = '5464564596999.5534733'
    puts "sum of BigDecimals: #{BigDecimal(a) + BigDecimal(b)}"
    # sum = 95745741100319272466.9987078234546
    expect(add(a, b)).to eq(BigDecimal(a) + BigDecimal(b))
  end
end

# OUTPUT:
#
# int1: 512, int2: 25 | dec1: 349, dec2: 67
# dec_index: 0, int_index: -1
# int_sum: 0.7e1
# int_sum + dec_sum: 0.79e1

# int1: 512, int2: 25 | dec1: 349, dec2: 67
# dec_index: 1, int_index: -2
# int_sum: 0.379e2
# int_sum + dec_sum: 0.3801e2

# int1: 512, int2: 025 | dec1: 349, dec2: 670
# dec_index: 2, int_index: -3
# int_sum: 0.53801e3
# int_sum + dec_sum: 0.538019e3

# ----------------------
# int1: 25, int2: 512 | dec1: 67, dec2: 349
# dec_index: 0, int_index: -1
# int_sum: 0.7e1
# int_sum + dec_sum: 0.79e1

# int1: 25, int2: 512 | dec1: 67, dec2: 349
# dec_index: 1, int_index: -2
# int_sum: 0.379e2
# int_sum + dec_sum: 0.3801e2

# int1: 025, int2: 512 | dec1: 670, dec2: 349
# dec_index: 2, int_index: -3
# int_sum: 0.53801e3
# int_sum + dec_sum: 0.538019e3

# ----------------------
# int1: 23423, int2: 0 | dec1: 97655, dec2: 3668558
# dec_index: 0, int_index: -1
# int_sum: 0.3e1
# int_sum + dec_sum: 0.42e1

# int1: 23423, int2: 00 | dec1: 97655, dec2: 3668558
# dec_index: 1, int_index: -2
# int_sum: 0.242e2
# int_sum + dec_sum: 0.2433e2

# int1: 23423, int2: 000 | dec1: 97655, dec2: 3668558
# dec_index: 2, int_index: -3
# int_sum: 0.42433e3
# int_sum + dec_sum: 0.424342e3

# int1: 23423, int2: 0000 | dec1: 97655, dec2: 3668558
# dec_index: 3, int_index: -4
# int_sum: 0.3424342e4
# int_sum + dec_sum: 0.34243433e4

# int1: 23423, int2: 00000 | dec1: 97655, dec2: 3668558
# dec_index: 4, int_index: -5
# int_sum: 0.234243433e5
# int_sum + dec_sum: 0.234243434e5

# int1: 023423, int2: 000000 | dec1: 976550, dec2: 3668558
# dec_index: 5, int_index: -6
# int_sum: 0.234243434e5
# int_sum + dec_sum: 0.23424343405e5

# int1: 0023423, int2: 0000000 | dec1: 9765500, dec2: 3668558
# dec_index: 6, int_index: -7
# int_sum: 0.23424343405e5
# int_sum + dec_sum: 0.234243434058e5

# ----------------------
# sum of BigDecimals: 0.957457411003192724669987078234546e20
# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733
# dec_index: 0, int_index: -1
# int_sum: 0.16e2
# int_sum + dec_sum: 0.169e2

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733
# dec_index: 1, int_index: -2
# int_sum: 0.1669e3
# int_sum + dec_sum: 0.16699e3

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733
# dec_index: 2, int_index: -3
# int_sum: 0.146699e4
# int_sum + dec_sum: 0.1466998e4

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733
# dec_index: 3, int_index: -4
# int_sum: 0.12466998e5
# int_sum + dec_sum: 0.124669986e5

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733
# dec_index: 4, int_index: -5
# int_sum: 0.1724669986e6
# int_sum + dec_sum: 0.1724669987e6

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733
# dec_index: 5, int_index: -6
# int_sum: 0.12724669987e7
# int_sum + dec_sum: 0.1272466998707e7

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733
# dec_index: 6, int_index: -7
# int_sum: 0.9272466998707e7
# int_sum + dec_sum: 0.92724669987078e7

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 55347330
# dec_index: 7, int_index: -8
# int_sum: 0.1192724669987078e9
# int_sum + dec_sum: 0.11927246699870782e9

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 553473300
# dec_index: 8, int_index: -9
# int_sum: 0.131927246699870782e10
# int_sum + dec_sum: 0.1319272466998707823e10

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733000
# dec_index: 9, int_index: -10
# int_sum: 0.10319272466998707823e11
# int_sum + dec_sum: 0.103192724669987078234e11

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 55347330000
# dec_index: 10, int_index: -11
# int_sum: 0.1003192724669987078234e12
# int_sum + dec_sum: 0.10031927246699870782345e12

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 553473300000
# dec_index: 11, int_index: -12
# int_sum: 0.110031927246699870782345e13
# int_sum + dec_sum: 0.1100319272466998707823454e13

# int1: 95745735635754675467, int2: 5464564596999 | dec1: 4452345234546, dec2: 5534733000000
# dec_index: 12, int_index: -13
# int_sum: 0.11100319272466998707823454e14
# int_sum + dec_sum: 0.111003192724669987078234546e14

# int1: 95745735635754675467, int2: 05464564596999 | dec1: 44523452345460, dec2: 55347330000000
# dec_index: 13, int_index: -14
# int_sum: 0.411003192724669987078234546e14
# int_sum + dec_sum: 0.411003192724669987078234546e14

# int1: 95745735635754675467, int2: 005464564596999 | dec1: 445234523454600, dec2: 553473300000000
# dec_index: 14, int_index: -15
# int_sum: 0.7411003192724669987078234546e15
# int_sum + dec_sum: 0.7411003192724669987078234546e15

# int1: 95745735635754675467, int2: 0005464564596999 | dec1: 4452345234546000, dec2: 5534733000000000
# dec_index: 15, int_index: -16
# int_sum: 0.57411003192724669987078234546e16
# int_sum + dec_sum: 0.57411003192724669987078234546e16

# int1: 95745735635754675467, int2: 00005464564596999 | dec1: 44523452345460000, dec2: 55347330000000000
# dec_index: 16, int_index: -17
# int_sum: 0.457411003192724669987078234546e17
# int_sum + dec_sum: 0.457411003192724669987078234546e17

# int1: 95745735635754675467, int2: 000005464564596999 | dec1: 445234523454600000, dec2: 553473300000000000
# dec_index: 17, int_index: -18
# int_sum: 0.7457411003192724669987078234546e18
# int_sum + dec_sum: 0.7457411003192724669987078234546e18

# int1: 95745735635754675467, int2: 0000005464564596999 | dec1: 4452345234546000000, dec2: 5534733000000000000
# dec_index: 18, int_index: -19
# int_sum: 0.57457411003192724669987078234546e19
# int_sum + dec_sum: 0.57457411003192724669987078234546e19

# int1: 95745735635754675467, int2: 00000005464564596999 | dec1: 44523452345460000000, dec2: 55347330000000000000
# dec_index: 19, int_index: -20
# int_sum: 0.957457411003192724669987078234546e20
# int_sum + dec_sum: 0.957457411003192724669987078234546e20