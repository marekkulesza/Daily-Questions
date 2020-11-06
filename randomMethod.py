# Make a method that returns a value
# then loop that method, use the return

import random

# This method uses the randint method with 1 
# parameter to get a random number between 0-number
def ranInt(lastnum):
    ranIntnum = random.randint(0,lastnum)
    print("The random number is:",ranIntnum)
    return ranIntnum

# Loop the method over and over again until the number
# equals 0, then break the loop
while True:
    variable1 = ranInt(int(input("Give me a number: ")))
    if variable1 == 0:
        break
