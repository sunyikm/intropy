max([1,2,3,4,5])

def neg(x):
    return -x
max([1,2,3,4,5], key=neg)

def count_vowels(s:str) -> int:
    return sum([1 for c in s if c in 'aeiou'])

names = ["buzz", "rex", "bo", "hamm", "slink", "potato", "woody", "sarge",
         "etch", "lenny", "squeeze", "wheezy", "jessie", "stretch", "buster",
         "bullseye", "bookworm", "trixie", "sid"]

max_vowel_word = max(names, key=count_vowels)
print(f"包含最多元音祖母的单词是{max_vowel_word}")