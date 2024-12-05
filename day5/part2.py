from collections import defaultdict

import numpy as np

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


def handle_sequence(numbers):

    for index, elem in enumerate(numbers):
        if has_ilegal_ahead(elem, index, numbers):
            return False
    return True


def fix_sequence(numbers):

    while not handle_sequence(numbers):
        for index, elem in enumerate(numbers):
            for i in range(index + 1, len(numbers)):
                if numbers[i] in rules[elem]:
                    numbers[i], numbers[index] = numbers[index], numbers[i]
    return numbers

def main():
    input_file = open("input.txt", "r")
    count = 0
    bad_sequences = []
    fixed = []
    for line in input_file:
        line = line.strip()
        if "|" in line:
            handle_rule(line)
        if "," in line:
            numbers = [int(a) for a in line.split(",")]
            if not handle_sequence(numbers):
                bad_sequences.append(fix_sequence(numbers))
                count += 1

    for bad_sequence in bad_sequences:
        fixed.append(fix_sequence(bad_sequence))


    print(count)
    sum = 0
    for sequence in bad_sequences:
        # print
        sum += sequence[len(sequence) // 2]

    print(bad_sequences)
    print(sum)

main()
