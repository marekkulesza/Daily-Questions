# Task Given an array of integers ,
# Find the minimum sum which is 
# obtained from summing each Two 
# integers product .

# minSum({5,4,2,3}) ==> return (22) 
# The minimum sum obtained from summing 
# each two integers product , 5*2 + 3*4 = 22

def min_sum(lst):

    anslst = []
    counter1 = 0
    counter2 = len(lst)-1
    lst.sort()

    while True:

        ansSum = lst[counter1]*lst[counter2]
        anslst.append(ansSum)

        counter1 += 1
        counter2 -= 1
        
        if counter1 > counter2:
            return sum(anslst)


    


print(min_sum([5,4,2,3])) 