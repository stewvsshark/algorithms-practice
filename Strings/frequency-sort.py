
# Given a string s, sort it in decreasing order based on the frequency of the characters.
#   The frequency of a character is the number of times it appears in the string.
#
# Return the sorted string. If there are multiple answers, return any of them.
# Case sensitive
#
# tree -> eert or eetr
# Aabb -> bbAa or bbaA

def frequency_sort(s):
    frequencies = {}
    for letter in s:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1

    sorted_dict = {k: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}
    output_str = ''
    for letter in sorted_dict:
        output_str += (letter * frequencies[letter])

    return output_str


s = "tree"
print(frequency_sort(s))