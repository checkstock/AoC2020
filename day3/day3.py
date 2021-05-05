input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.strip())

rows = len(input)
columns = len(input[0])

print("Day 3 Part 1: ")

column_index = 0
trees = 0

for x in range(0, rows):
        if input[x][column_index] == '#':
            trees += 1

        column_index = (column_index + 3) % columns

print("We encountered", trees, "trees.\n")