
# One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount.
# Rotating a character means replacing it with another character that is a
#   certain number of steps away in normal alphabetic or numerical order.
# For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?".
# Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A),
#   and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0).
# Note that the non-alphanumeric characters remain unchanged.
# Given a string and a rotation factor, return an encrypted string.

# Things to looked up
# 1. some_string.index(substr)
# 2. Cannot perform arithmetic on char ints
# 3. Helper methods must be declared above driver methods

# Questions:
# 1. Is this case sensitive?
# 2. Is the rotation factor >= 0?
# 3. Define lookup array ahead of time?

# Optimizations
# 1. Calculate new index based on type with helper function
# 2. Calculate length of comparison arrays once

# Runtime
# Time: o(N) where n is the length of the input string
# Space: o(N) where n is the length of the input string

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

def get_new_index(char, compare_str, rotation_factor):
    i = compare_str.index(char)
    new_index = i + rotation_factor
    if new_index > len(compare_str):
        new_index = new_index % len(compare_str)
    return new_index


def rotational_cipher(input_str, rotation_factor):
    output_str = ""
    for char in input_str:
        if char.isalpha():
            new_index = get_new_index(char.lower(), alphabet, rotation_factor)

            if char.islower():
                output_str += alphabet[new_index]
            elif char.isupper():
                output_str += alphabet[new_index].upper()

        elif char.isnumeric():
            new_index = get_new_index(char, numbers, rotation_factor)
            output_str += numbers[new_index]

        else:
            output_str += char

    return output_str


print(rotational_cipher("Zebra-493?", 3))
print(rotational_cipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))
print(rotational_cipher("All-convoYs-9-be:Alert1.", 4))
print(rotational_cipher("abcdZXYzxy-999.@", 200))
