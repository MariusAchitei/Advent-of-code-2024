from collections import defaultdict

import numpy as np


def count_in_joined_line(line: str):
    return line.count("XMAS") + line.count("SAMX")


def count_on_lines(matrix: list):
    return sum(list(map(lambda line: count_in_joined_line("".join(line)), [line for line in matrix])))


def count_on_columns(matrix):
    transposed = np.transpose(matrix)
    return count_on_lines(list(transposed))


def count_above_first(matrix):
    diagonal_lines = defaultdict(list)
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix[i])):
            if str(i - j) in diagonal_lines:
                diagonal_lines[i - j] = [matrix[i][j]]
            else:
                diagonal_lines[i - j].append(matrix[i][j])
    print("above first")
    for a in list(diagonal_lines.values()):
        print("".join(a))
    # input()
    return count_on_lines(list(diagonal_lines.values()))


def count_below_first(matrix):
    diagonal_lines = defaultdict(list)
    for i in range(0, len(matrix)):
        for j in range(0, i):
            if str(i - j) in diagonal_lines:
                diagonal_lines[i - j] = [matrix[i][j]]
            else:
                diagonal_lines[i - j].append(matrix[i][j])
    print("below first")
    for a in list(diagonal_lines.values()):
        print("".join(a))
    #     input()
    return count_on_lines(list(diagonal_lines.values()))


def count_on_first_diagonal(matrix):
    return count_above_first(matrix) + count_below_first(matrix)


def count_above_second(matrix):
    diagonal_lines = defaultdict(list)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i]) - i):
            if str(i + j) in diagonal_lines:
                diagonal_lines[i + j] = [matrix[i][j]]
            else:
                diagonal_lines[i + j].append(matrix[i][j])
    print("------------")
    print(diagonal_lines.keys())
    print("above second")
    for a in list(diagonal_lines.values()):
        print("".join(a))
    #     input()
    return count_on_lines(list(diagonal_lines.values()))


def count_below_second(matrix):
    diagonal_lines = defaultdict(list)
    for i in range(0, len(matrix)):
        for j in range(len(matrix[i]) - i, len(matrix[i])):
            if str(i + j) in diagonal_lines:
                diagonal_lines[i + j] = [matrix[i][j]]
            else:
                diagonal_lines[i + j].append(matrix[i][j])
    print("below second")
    for a in list(diagonal_lines.values()):
        print("".join(a))
    #     input()
    return count_on_lines(list(diagonal_lines.values()))


def count_on_second_diagonal(matrix):
    return count_above_second(matrix) + count_below_second(matrix)


def main():
    matrix = []
    input_file = open("input.txt", "r")
    for line in input_file:
        # Print each line
        char_arr = []
        char_arr.extend(line.strip())
        matrix.append(char_arr)

    lines = count_on_lines(matrix)
    columns = count_on_columns(matrix)
    first_diagonal = count_on_first_diagonal(matrix)
    second_diagonal = count_on_second_diagonal(matrix)

    print(lines, columns, first_diagonal, second_diagonal)

    print(lines + columns + first_diagonal + second_diagonal)


main()
