import re

from numpy.matlib import empty


def extract_factors_from_string(operation):
    pattern = "\d+"
    matches = re.findall(pattern, operation)
    return (matches[0], matches[1])


def process_input(line):
    sum = 0
    pattern = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, line)
    previous_comand = True
    for match in matches:
        if match[0] and previous_comand:
            x1, x2 = extract_factors_from_string(match[0])
            print(x1, x2)
            sum += int(x1) * int(x2)
            continue
        if match[1]:
            previous_comand = True
        if match[2]:
            previous_comand = False
    print(sum)

def main():
    input_file = open("input.txt", "r")
    lines = list()
    for line in input_file:
        lines.append(line)
    process_input("".join(lines))


main()