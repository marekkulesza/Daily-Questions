def multiplication_table(size):
    gridList = []
    for rows in range(1,size+1):
        # print("rows ", rows)
        columnsList = []

        for columns in range(1,size+1):
            # print("columns ", columns)
            columnsList.append(columns*rows)
        
        gridList.append(columnsList)

    # print("columnsList ", columnsList)
    # print("rowsList ", rowsList)
    # print("numberTable ", numberTable)
    return gridList

print(multiplication_table(4))