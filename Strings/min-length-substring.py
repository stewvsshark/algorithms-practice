
# You are given two strings s and t.
# You can select any substring of string s and rearrange the characters of the selected substring.
# Determine the minimum length of the substring of s such that string t is a substring of the selected substring.

# Insights
# 1. substring must be of length t
# 2. All we need to find is that s contains a continuous substring containing the constituent parts of t
#   and return the length of thet substring


# Example
# s = "dcbefebce"
# t = "fd"
# output = 5

def min_lengh_substring(s, t):
    s_len = len(s)
    t_len = len(t)

    if t_len > s_len:
        return -1

    instances_of_t_chars = {}
    for char in t:
        if instances_of_t_chars.get(char):
            instances_of_t_chars[char] += 1
        else:
            instances_of_t_chars[char] = 1

    start_index = -1
    end_index = -1
    for i in range(s_len):
        if instances_of_t_chars.get(s[i]) and instances_of_t_chars.get(s[i]) > 0:
            instances_of_t_chars[s[i]] -= 1
            if start_index == -1:
                start_index = i

        if max(instances_of_t_chars.values()) == 0 and end_index == -1:
            end_index = i

    if start_index != -1 and end_index != -1:
        return end_index-start_index + 1

    return -1


s1 = "dcbefebce"
t1 = "fd"
print(min_lengh_substring(s1, t1))

s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
t2 = "cbccfafebccdccebdd"
print(min_lengh_substring(s2, t2))