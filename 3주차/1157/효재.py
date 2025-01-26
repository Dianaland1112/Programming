word = input()
word = word.upper()
word_dict = {}

for char in word:
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 1

max_value = max(word_dict.values())

max_keys = []
for key, value in word_dict.items():
    if value == max_value:
        max_keys.append(key)

if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0])