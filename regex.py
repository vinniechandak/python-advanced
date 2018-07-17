# Starting with Regex #
# First thing to import the 're' module #

import re

# string literal matches strings.

pattern = re.compile('a')
x = pattern.match('a')
print(x)

pattern = re.compile('ab')
x = pattern.match('ab')
print(x.group())
print(x)

# reccuring patterns '+' used for 1 or n matches. '*' used for 0 or n matches.

pattern = re.compile('ab+')
x = pattern.match('abbbbb')
print(x)
x = pattern.match('ab')
print(x)

pattern = re.compile('ab*')
x = pattern.match('abababababababab')
print(x)
x = pattern.match('a')
print(x)

# alternate pattern matching. separated by '|'

pattern = re.compile('aaa|bbb')
x = pattern.match('aaa')
print(x)
x = pattern.match('bbb')
print(x)
x = pattern.match('abab')
print(x)

# to match characters in a range or as a individual put them in [] brackets.
# this matches 'a','b' or 'c' or any number between 0 to 9.
pattern = re.compile('[abc]|[0-9]')
x = pattern.match('apqr')
print(x)
x = pattern.match('12hye')
print(x)

# '\d' represents only numerics, '\w' represents alphanumerics and '\W' represents non-numeric alpha characters.
pattern = re.compile('(\d)*')
x = pattern.match('2365634254')
print(x)

pattern = re.compile('(\w)*')
x = pattern.match('2365akfjasf4254')
print(x)

pattern = re.compile('(\W)*')
x = pattern.match('2365$3%%&&*54')
print(x)

# basic regex ends :P :) :D #
