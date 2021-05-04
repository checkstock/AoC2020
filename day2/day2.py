input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.strip())

for x in range(0, len(input)):
    print(input[x])