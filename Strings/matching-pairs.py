
# Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s
#   and t after swapping exactly two characters within s.
# A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the
#   ith and jth index of s, respectively. The matching pairs of the two strings are defined as the
#   number of indices for which s[i] and t[i] are equal.
# Note: This means you must swap two characters at different indices.

# Example 1
# s = "abcd"
# t = "adcb"
# output = 4

# Lookup
# 1. strings are immutable

# Approach/insights:
# 1. Keyword: pairs indicates maybe a tuple is of use
# 2. You MUST swap two pairs even if it yields a worse result -
def matching_pairs(s, t):
    s_len = len(s)
    if s == t:
        return s_len - 2

    unmatched_pairs = set()
    unmatched_in_t = set()
    unmatched_in_s = set()

    result = 0
    full_swap = False
    partial_swap = False

    i = 0
    while i < s_len or not full_swap:
        if s[i] == t[i]:
            result += 1

        if s[i] != t[i]:
            unmatched_pairs.add((s[i], t[i]))
            unmatched_in_t.add(t[i])
            unmatched_in_s.add(s[i])

            if (t[i], s[i]) in unmatched_pairs:
                full_swap = True

            elif s[i] in unmatched_in_t or t[i] in unmatched_in_s:
                partial_swap = True

        i += 1

    if full_swap:
        return result + 2
    elif partial_swap:
        return result + 1

    return result


s_1, t_1 = "abcde", "adcbe"
s_2, t_2 = "abcd", "abcd"

print(matching_pairs(s_1, t_1))
print(matching_pairs(s_2, t_2))
