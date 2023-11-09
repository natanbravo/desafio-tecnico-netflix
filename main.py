"""
Given a string 's' consisting od small English letters, find and return the first instance of a non-repeating
character in it. If there is no such character, return '_'

Example: 
    . For (s = "abacabad"), the output should be (solution(s) = 'c').
    There are no '2' non-repeating characters in the strig: 'c' and 'd'. Return (c) since it appears in the string first.

    . For (s = "abacabaabacaba"), the output should be (solution(s) = '_').
    There are no characters in this string that do not repeat.
"""


def solution(value):
    char_list = list(value)
    char_str = ''
    new_char_list = []

    for item in char_list:
        char_str = item

        if char_list.count(char_str) == 1:
            new_char_list.append(char_str)

    if len(new_char_list) > 0:
        return new_char_list[0]
    else:
        return '_'


s = "abacabad"
# s = "abacabaabacaba"

print(solution(s))
