tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
def printTable(tableData):
    colWidths = [0] * len(tableData)
    for columns in range(len(tableData)):
        for items in range(columns):
            if len(tableData[columns][items]) > colWidths[columns]:
                colWidths[columns] = len(tableData[columns][items])
    print(colWidths)
    
printTable(tableData)
