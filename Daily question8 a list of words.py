new_list = words
a_list = []

for elements in new_list:
    if elements[0] == 'a':
        a_list.append(elements)
    if elements[0] == "A":
        a_list.append(elements)

print(a_list)