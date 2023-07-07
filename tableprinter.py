tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        max = 0
        for x in range(len(tableData[i])):
            if len(tableData[i][x]) > max:
                max = len(tableData[i][x])
        colWidths[i] = int(max)
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(colWidths[x]), end=" ")
        print("\n")
printTable(tableData)
