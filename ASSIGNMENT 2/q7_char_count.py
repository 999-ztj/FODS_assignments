"""
This program counts characters in a sentence excluding spaces.
"""

def key_value(sentence):
    result = {}
    for ch in sentence:
        if ch != " ":
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1
    return result

sentence = input("Enter a sentence: ")
print(key_value(sentence))