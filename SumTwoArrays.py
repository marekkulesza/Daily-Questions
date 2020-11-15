def sum_arrays(array1,array2):

    if len(array1) == 0 and len(array2) == 0:
        return []

    if len(array1) == 0 and len(array2) > 0: 

        strList2 = ""

        for element2 in array2:
            strList2 += str(element2)
        summedList = int(strList2)
        if summedList < 0:
            ans = list(map(int,(str(abs(summedList)))))
            ans[0] = "-"+str(ans[0])
            yeet = int(ans[0])
            ans.insert(0,yeet)
            ans.remove(ans[1])
            return ans
            
        ans = list(map(int,str(summedList)))
        return ans

    if len(array1) > 0 and len(array2) == 0: 

        strList1 = ""

        for element1 in array1: 
            strList1 += str(element1)  #  123332245
        summedList = int(strList1)
        if summedList < 0:
            ans = list(map(int,(str(abs(summedList)))))
            ans[0] = "-"+str(ans[0])
            yeet = int(ans[0])
            ans.insert(0,yeet)
            ans.remove(ans[1])
            return ans     
        ans = list(map(int,str(summedList)))    
        return ans

    strList1 = ""
    strList2 = ""

    for element1 in array1:
        strList1 += str(element1)
    for element2 in array2:
        strList2 += str(element2)

    summedList = int(strList1) + int(strList2)
    
    if summedList < 0:
        ans = list(map(int,(str(abs(summedList)))))
        ans[0] = "-"+str(ans[0])
        yeet = int(ans[0])
        ans.insert(0,yeet)
        ans.remove(ans[1])
        return ans

    ans = list(map(int,(str(summedList)))) 
    return ans

#print(sum_arrays([],[1,2,3]))
print(sum_arrays([-4, 6, 0, 8, 6, 9], [9, 4, 8, 7, 5]))