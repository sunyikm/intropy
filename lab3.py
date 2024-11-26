
#ex3.3
# n=int(input("Enter a number: "))

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         result=i*j
#         # print(str(result).rjust(3), end=" ")
#         print(f"{result:>3}", end=" ")
#     print()       

#ex3.4


#ex3.8
# s=input("Enter a string: ")
# n=int(input("Enter a number: "))

# encrypted=""

# for character in s:
#     code = ord(character)
#     if ord("A") <= code <= ord("Z"):
#         encrypted = encrypted + chr(ord('A')+ (code-ord('A')+n)%26)
#     elif ord("a") <= code <= ord("z"):
#         encrypted = encrypted + chr(ord('a')+ (code-ord('a')+n)%26)
#     else:
#         encrypted = encrypted + character

# print("Encrypted: ", encrypted)      


#ex3.9
# with open('example.txt',encoding='utf-8') as file:
#     text = file.read()
#     print(text)

#ex3.10
# with open('three_musketeers.txt',encoding='utf-8') as f:
#     lines=f.readlines()

# line_count=len(lines)

# print(f"Number of lines: {line_count}")

#ex3.11
# with open('three_musketeers.txt',encoding='utf-8') as f:
#     text=f.read()

#     word_count=len(text.split())
#     print(f"Number of words: {word_count}")

#ex3.12
# with open('three_musketeers.txt',encoding='utf-8') as f:
#     text=f.read()

#     char_count=len(text)
#     print(f"Number of characters: {char_count}")

#ex3.13
# with open('three_musketeers.txt',encoding='utf-8') as f:
#     text=f.read()

#     vowel_count=0

#     vowels= "aeiouAEIOU"

#     for vowel in vowels:
#         vowel_count+=text.count(vowel)

#     print(f"Number of vowels: {vowel_count}")

#ex3.14
with open('three_musketeers.txt',encoding='utf-8') as f:
    text=f.read()

frequency={}

for char in text:
    code=ord(char)
    if ord('A')<=code<=ord('Z') or ord('a')<=code<=ord('z'):
        letter=char.lower()
        if letter in frequency:
            frequency[letter]+=1
        else:
            frequency[letter]=1

frequency_list=[(freq, letter) for letter, freq in frequency.items()]

sorted_frequency=