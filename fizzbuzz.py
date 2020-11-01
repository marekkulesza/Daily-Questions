# Fizzbuzz

numRange = list(range(51))
ansList1 = []
ansList2 = []

for element in numRange:
    if element % 3 == 0 and element % 5 == 0:
        ansList1.append("fizzbuzz")
    elif element % 5 == 0:
        ansList1.append("buzz")
    elif element % 3 == 0:
        ansList1.append("fizz")
    else:
        ansList1.append(element)
    
print(ansList1)

print(""" ******* list 2 ******** """)


num = 0
while True:
    if num % 15 == 0:
        ansList2.append("fizzbuzz")
    elif num % 5 == 0:
        ansList2.append("buzz")
    elif num % 3 == 0:
        ansList2.append("fizz")
    else:
        ansList2.append(num)
    num += 1

    if num == 51:
        break

print(ansList2)

if ansList1 == ansList2:
    print("""
    Correct
    """)