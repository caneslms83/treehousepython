def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter.lower() in vowels:
            word = word.replace(letter, "")
    return word

print(disemvowel("This is A tEst afadfadf AVAVAAVA"))