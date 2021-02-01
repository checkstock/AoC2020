with open("input.txt") as file:
    input = file.read().strip()

input = [int(x) for x in input.split("\n")]

print("Part 1:")

for x in range(0, len(input)):
    a = input[x]

    for y in range(x+1, len(input)):
        b = input[y]

        if a + b == 2020:

            print("A: ", a)
            print("B: ", b)
            print("Answer: ", a * b, "\n")
            break

print("Part 2:")

for x in range(0, len(input)):
    a = input[x]

    for y in range(x+1, len(input)):
        b = input[y]

        for z in range(y+1, len(input)):
            c = input[z]

            d = a + b + c

            if a + b + c == 2020:

                print("A: ", a)
                print("B: ", b)
                print("C: ", c)
                print("Answer: ", a * b * c)
                break