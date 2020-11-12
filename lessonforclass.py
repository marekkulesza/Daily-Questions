num = float(5)
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# Simplify this bit of code
x = 1
if x > 0 and x < 0:
    print("Its zero")
else:
    print("this is not zero")

# if x == 0:
num = int(6)
if num >= 5:
    if num <= 10:
        print("Your number is inbetween 5 and 10 :)")

if num >= 5 and num <= 10:
    print("Your number is inbetween 5 and 10 :)")


counter1 = 0
while True:
    counter1 = counter1 + 1
    print("I love you")
    if counter1 > 5:
        break

counter = 0
flag = True
while flag:  # You can do while True: but for C# we set flag = True since while
    counter = counter + 1
    print("I love you")
    if counter > 5:
        flag = False  # Sentinal Value terminates the loop, ends the loop

print()

counter2 = 0
while counter2 < 5:
    counter2 += 1

    print("I love you")

# counter = counter + 1
# counter += 1


# EXAMPLE 3 PART 2
choice = "NO MORE"  # choice is the SENTINEL
faves = []  # list

# Since the input() function doesn't allow commas, we need to concatenate the sentinel into the user prompt
prompt = "What is one of your favourite things? Enter '" + choice + "' to stop: "

# Use the string variable called "prompt" as what we print to the user
newFave = input(prompt)

while newFave != choice:
    faves.append(newFave)
    newFave = input(prompt)

# Once the while loops exits, we are done asking about favourite things,
# We want to print it out in order, so we print faves[0]
index = 0

while index < len(faves):
    print(faves[index])
    index = index + 1  # Don't forget to update the loop variable!
        

