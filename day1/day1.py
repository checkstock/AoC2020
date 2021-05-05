with open("input.txt") as file:
    input = file.read().strip()

input = [int(x) for x in input.split("\n")]
lines = len(input)

print("Part 1:")

for i in range(0, lines):
    a = input[i]

    for j in range(i+1, lines):
        b = input[k]

        if a + b == 2020:
            print("A: ", a)
            print("B: ", b)
            print("Answer: ", a * b, "\n")
            break

print("Part 2:")

for i in range(0, lines):
    a = input[i]

    for j in range(i+1, lines):
        b = input[k]

        for k in range(j+1, lines):
            c = input[j]

            if a + b + c == 2020:
                print("A: ", a)
                print("B: ", b)
                print("C: ", c)
                print("Answer: ", a * b * c)
                break