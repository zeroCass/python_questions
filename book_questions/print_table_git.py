
'''
Algumas solucoes encontradas no git/stackOverflow sobre a questao
Serviu-se de comparação para ver se a minha solucao estava correta base
'''

def printTable(tableData):
    colWidths = [0] * len(tableData)

    for i, columnData in enumerate(tableData):
        for rowItem in columnData:
            itemLength = len(rowItem)
            if itemLength > colWidths[i]:
                colWidths[i] = itemLength
                
    numCols = len(tableData)
    numRows = len(tableData[0])
                  
    for rowIndex in range(numRows):
        for colIndex in range(numCols):
            print(tableData[colIndex][rowIndex].rjust(colWidths[colIndex]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# printTable(tableData)



def printTable(inputList):
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(inputList)):
	    for j in range(len(inputList[i])):
		    if len(inputList[i][j]) > colWidths[i]:
			    colWidths[i] = len(inputList[i][j])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in colWidths
    for x in range(len(inputList[0])):
	    for y in range(len(inputList)):
		    print(inputList[y][x].rjust(colWidths[y]), end = ' ')
	    print('')



tableData = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)