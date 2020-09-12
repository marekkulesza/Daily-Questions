inputstring = input()
vowels = ['a','e','i','o','u']
vowelslist = []

for element in inputstring:
    if element in vowels:
        vowelslist.append(element)
print(vowelslist)