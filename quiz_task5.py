f = open("lorem.txt", 'r')

char_dict = {}

for word in f:
    for char in word.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

print(char_dict)
