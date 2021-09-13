word1, word2 = input("enter two words\n").split()

set1 = set(word1)
set2 = set(word2)

T = len(set1.intersection(set2)) / (len(set1) + len(set2) - len(set1.intersection(set2)))
print(T)