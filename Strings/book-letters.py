import math

# How many facebook 'stickers' do I need to make the following words and phrases?

# Things I looked up:
# .lower()
# isalpha()
# max(dictionary.values() returns the max value

# Possible questions:
# 1. Do I need to solve for a generic input string
# 2. Can I assume all the letters in the input string occur at least once in 'facebook'
# 3.  Do I need to handle punctuation?
# 4. Do I need to handle case?

# Possible optimizations
# 1. Move source string out of method so it only needs to be called once


def num_of_sticker(input_string):
    letter_count = {}
    for char in "facebook":
        letter_count[char] = 0
    for char in input_string:
        if char.isalpha():
            letter_count[char] += 1

    letter_count['o'] = math.floor(letter_count['o']/2)

    return max(letter_count.values())


print(num_of_sticker("book"))
print(num_of_sticker("fab face fook"))
print(num_of_sticker("oo oo oo ooo"))


