"""
Problem: Capitalize
Pattern: Fundamentals (string manipulation)
Time: O(n) | Space: O(n)

Capitalize the first letter of every word in a sentence.

Input:  "hi there, how is it going?"
Output: "Hi There, How Is It Going?"
"""

def capitalize(input_str):
    return ' '.join(word[0].upper() + word[1:] if word else word for word in input_str.split(' '))


# Alternative: Python's built-in str.title() looks similar but also
# lowercases the rest of each word AND capitalizes after punctuation like
# apostrophes (e.g. "it's" -> "It'S"), which is usually wrong. This explicit
# loop version avoids that gotcha while doing the same O(n) work.
def capitalize_loop(input_str):
    if input_str == '':
        return input_str
    words = input_str.split(' ')
    for i in range(len(words)):
        if words[i]:
            words[i] = words[i][0].upper() + words[i][1:]
    return ' '.join(words)


if __name__ == "__main__":
    print(capitalize("hi there, how is it going?"))  # Hi There, How Is It Going?
