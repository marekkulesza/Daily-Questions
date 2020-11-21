

one_ancestor = "Extrater"
other_ancestor = "Yooo"

# Calculate the identity of a new alien here



#new_alien = one_ancestor[0:len(one_ancestor)//2] + other_ancestor[0:len(other_ancestor)//2]
#print(new_alien)
new_alien = (id(one_ancestor) + id(other_ancestor))//2
print(new_alien)


def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        if str(id(i)).endswith("888"):
            return i

print(object_with_beautiful_identity())