with open("input.txt") as file:
    input = file.read().strip()

input = [int(x) for x in input.split("\n")]
lines = len(input)

print("Part 1:")

for x in range(0, lines):
    a = input[x]

    for y in range(x+1, lines):
        b = input[y]

        if a + b == 2020:
            print("A: ", a)
            print("B: ", b)
            print("Answer: ", a * b, "\n")
            break

print("Part 2:")

for x in range(0, lines):
    a = input[x]

    for y in range(x+1, lines):
        b = input[y]

        for z in range(y+1, lines):
            c = input[z]

            if a + b + c == 2020:
                print("A: ", a)
                print("B: ", b)
                print("C: ", c)
                print("Answer: ", a * b * c)
                break