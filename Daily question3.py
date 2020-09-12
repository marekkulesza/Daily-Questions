inputstring = input()

vowels = ['a','e','i','o','u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for element in inputstring:
    if element in vowels:
        print("vowel")
    if element in consonant:
        print("consonant")
    elif element not in vowels and element not in consonant:
        break
