word_length = 0
cur_word_length = 0
longest_word = ""

f = open("words.txt", 'r')

for word in f:
    cur_word_length = len(word)
    if cur_word_length > word_length:
        longest_word = word
        word_length = cur_word_length

if word_length == 0:
    print("There is no words")
else:
    print(longest_word)
