originalGrid = [[0,0,0],[0,1,0],[0,0,0]]

for row in originalGrid:
    for item in row:
        if item == 1:
            row = [1,1,1]
            for newRow in originalGrid:
                newRow[row.index(item)] = 1
            print(originalGrid)