input = []

with open("input.txt") as file:
    for line in file:
        input.append(line.strip())

lines = len(input)

print("Day 2 Part 1: ")

valid_passwords = 0

for x in range(0, lines):
    letter_appears = 0

    split_input = input[x].split()
    numbers = split_input[0].split("-")

    min = int(numbers[0])

    max = int(numbers[1])

    required_letter = split_input[1].replace(':', "")

    password = split_input[2]

    for y in range(0, len(password)):
        if password[y] == required_letter:
            letter_appears += 1

    if letter_appears >= min and letter_appears <= max:
        valid_passwords += 1

print("There are", valid_passwords, "valid passwords. \n")


print("Day 2 Part 2: ")

valid_passwords = 0

for x in range(0, lines):
    split_input = input[x].split()
    numbers = split_input[0].split("-")

    index_one = int(numbers[0]) - 1
    index_two = int(numbers[1]) - 1

    required_letter = split_input[1].replace(":", "")

    password = split_input[2]

    exists_in_index_one = False
    exists_in_index_two = False

    if password[index_one] == required_letter and not password[index_two] == required_letter:
        valid_passwords += 1

    elif not password[index_one] == required_letter and password[index_two] == required_letter:
        valid_passwords += 1

print("There are", valid_passwords, "valid passwords.")