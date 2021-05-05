input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.strip())

rows = len(input)
columns = len(input[0])

print("Day 3 Part 1: ")
column_index = 0
trees = 0

for i in range(0, rows):
        if input[i][column_index] == '#':
            trees += 1

        column_index = (column_index + 3) % columns

print("We encountered", trees, "trees.\n")

print("Day 3 Part 2:")

product = 1

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for i in range(0, len(slopes)):
    column_index = 0
    row_index = 0
    trees = 0

    row_move = slopes[i][1]
    column_move = slopes[i][0]

    while row_index < rows:
        if input[row_index][column_index] == '#':
            trees += 1

        row_index += row_move
        column_index = (column_index + column_move) % columns

    print("The number of trees in slope", column_move, "," , row_move, "is", trees)

    product *= trees

print("The product of the number of trees we encountered in the 5 slopes is:", product)