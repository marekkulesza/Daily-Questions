# (test_it(0, 1), 0)
# (test_it(1, 2), 2)
# (test_it(5, 6), 30)
# (test_it(10, 10), 1)
# (test_it(200, 200), 4)
# (test_it(12, 34), 21)
# (test_it(123, 45), 54)




def test_it(a, b):

    a = str(a)
    b = str(b)
    suma = 0
    sumb = 0
    
    for element in a:
        suma = suma + int(element)

    for element in b:
        sumb = sumb + int(element)

    return suma * sumb


print(test_it(0, 1))    #0
print(test_it(1, 2))    #2
print(test_it(5, 6))    #30
print(test_it(10, 10))  #1 deletes the last num == 0
print(test_it(200, 200))#4
print(test_it(123, 45)) #54
