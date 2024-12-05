from collections import defaultdict

import numpy as np

rules = defaultdict(list)

good_sequences = []


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
    numbers = [int(a) for a in line.split(",")]

    for index, elem in enumerate(numbers):
        if has_ilegal_ahead(elem, index, numbers):
            return False
    return True


def main():
    input_file = open("input.txt", "r")
    count = 0
    for line in input_file:
        line = line.strip()
        if "|" in line:
            handle_rule(line)
        if "," in line:
            if handle_sequence(line):
                good_sequences.append([int (elem) for elem in line.split(",")])
                count += 1
    print(count)
    sum = 0
    for sequence in good_sequences:
        # print
        sum += sequence[len(sequence) // 2]

    print(good_sequences)
    print(sum)

main()
