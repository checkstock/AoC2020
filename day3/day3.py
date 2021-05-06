def find_trees(input, slope):
    rows = len(input)
    columns = len(input[0])

    row_index = 0
    column_index = 0

    row_move = slope[1]
    column_move = slope[0]

    trees = 0

    while row_index < rows:
        if input[row_index][column_index] == '#':
            trees += 1
        row_index += row_move
        column_index = (column_index + column_move) % columns

    return trees

def find_tree_products(input, slopes):
    product = 1

    for i in range(0, len(slopes)):
        product *= find_trees(input, slopes[i])

    return product

input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.strip())

print("Day 3 Part 1:")
print("We encountered", find_trees(input, [3, 1]), "trees.")

print("Day 3 Part 2:")
print("The product of all the trees in our 5 slopes is:", find_tree_products(input, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))