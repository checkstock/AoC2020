with open("input.txt") as file:
    input = file.read().strip()

input = [int(x) for x in input.split("\n")]
lines = len(input)

print("Part 1:")

for i in range(0, lines):

    for j in range(i+1, lines):

        if input[i] + input[j] == 2020:
            print("Answer: ", input[i] * input[j], "\n")
            break

print("Part 2:")

for i in range(0, lines):

    for j in range(i+1, lines):

        for k in range(j+1, lines):

            if input[i] + input[j] + input[k] == 2020:
                print("Answer: ", input[i] * input[j] * input[k])
                break