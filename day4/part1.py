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
    return generic_count_on_diagonal(matrix, lambda i: range(i, len(matrix[i])), lambda i, j: i - j)

def count_below_first(matrix):
    return generic_count_on_diagonal(matrix, lambda i: range(0, i), lambda i, j: i - j)


def count_on_first_diagonal(matrix):
    return count_above_first(matrix) + count_below_first(matrix)


def count_above_second(matrix):
    return generic_count_on_diagonal(matrix, lambda i: range(0, len(matrix[i])), lambda i, j: i + j)


def count_below_second(matrix):
    return generic_count_on_diagonal(matrix, lambda i: len(matrix[i]), lambda i, j: i + j)

def generic_count_on_diagonal(matrix, column_range_function, match_function):
    diagonal_lines = defaultdict(list)
    for i in range(0, len(matrix)):
        for j in column_range_function(i):
            if str(match_function(i, j)) in diagonal_lines:
                diagonal_lines[match_function(i, j)] = [matrix[i][j]]
            else:
                diagonal_lines[match_function(i, j)].append(matrix[i][j])
    return count_on_lines(list(diagonal_lines.values()))


def count_on_second_diagonal(matrix):
    return count_above_second(matrix) + count_below_second(matrix)


def main():
    matrix = []
    input_file = open("1/input.txt", "r")
    for line in input_file:
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
