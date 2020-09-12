#Write a program that takes three strings as input and 
# then constructs and prints a nested list from them – 
# with first string as a first element, a list containing 
# only second string as a second element and a list containing 
# another list containing a third string as a third element. 

str_1 = input() 
str_2 = input() 
str_3 = input() 

print([str_1 , [str_2] , [[str_3]]]) 