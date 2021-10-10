word = input().lower()

vowels = ['a', 'u', 'e', 'o', 'y', 'i']
vowels_counter = 0

for char in word:
    if char in vowels:
        vowels_counter += 1

print("vowels:", vowels_counter)
print("consonants:", len(word) - vowels_counter)