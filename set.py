vowels= set('aeiou')
word= input("provide a word:" )
found= set(vowels).intersection(set(word))

for vowel in found:
    print(vowel)