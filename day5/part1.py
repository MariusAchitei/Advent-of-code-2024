from collections import defaultdict

rules = defaultdict(list)


def handle_rule(line):
    first, second = [int(elem) for elem in line.split("|")]
    if second in rules:
        rules[second].append(first)
    else:
        rules[second] = [first]


def has_ilegal_ahead(elem, index, numbers):
    for i in range(index + 1, len(numbers)):
        if numbers[i] in rules[elem]:
            return True
    return False


def handle_sequence(line):
    numbers = extract_numbers(line)

    for index, elem in enumerate(numbers):
        if has_ilegal_ahead(elem, index, numbers):
            return False
    return True


def main():
    input_file = open("input.txt", "r")
    good_sequences = list()
    for line in input_file:
        line = line.strip()
        if "|" in line:
            handle_rule(line)
        if "," in line and handle_sequence(line):
            good_sequences.append(extract_numbers(line))

    middle_sum = sum(sequence[len(sequence) // 2] for sequence in good_sequences)

    print(good_sequences)
    print(middle_sum)


def extract_numbers(line):
    return [int(elem) for elem in line.split(",")]


main()
