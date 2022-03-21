

def frequencySort(s):
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
print(frequencySort(s))