letter = input("Input alphabet letter : ")
# vowels = {'a', 'e', 'i', 'o', 'u'}     # set
vowels = "aeiou"     # str
print(type(vowels))

if letter in vowels:     # in
    print(f'{letter} is a vowel~')
else:
    print(f'{letter} is a consonant!')