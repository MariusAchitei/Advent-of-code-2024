import numpy as np

directions = {"^": {"self": "^", "next": ">", "move": lambda i, j: (i - 1, j)},
              ">": {"self": ">", "next": "v", "move": lambda i, j: (i, j + 1)},
              "v": {"self": "v", "next": "<", "move": lambda i, j: (i + 1, j)},
              "<": {"self": "<", "next": "^", "move": lambda i, j: (i, j - 1)}}

original_matrix = []


def find_cursor(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in directions:
                return i, j, directions[matrix[i][j]]
    return None, None, None


def is_inside_matrix(matrix, i, j):
    if i is None or j is None:
        return False
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def is_obstacle(matrix, i, j, direction):
    return matrix[i][j] == "#"


a = set()


def move_cursor(matrix, i, j, direction):
    matrix[i][j] = direction["self"]


def move_cursor_game(matrix):
    direction_changes = set()
    i, j, direction = find_cursor(matrix)
    visited = set()
    while is_inside_matrix(matrix, i, j):
        nexti, nextj = direction["move"](i, j)
        if not is_inside_matrix(matrix, nexti, nextj):
            matrix[i][j] = "X"
            visited.add((i, j))
            break
        if is_obstacle(matrix, nexti, nextj, direction):
            direction = directions[direction["next"]]
            if (i, j, direction["self"]) in direction_changes:
                return i, j
            direction_changes.add((i, j, direction["self"]))
        else:
            oldi, oldj = i, j
            i, j = direction["move"](i, j)
            matrix[oldi][oldj] = "X"
            visited.add((oldi, oldj))
        move_cursor(matrix, i, j, direction)
    return None, None


def move_cursor_game_with_new_obstacle():
    new_positions = set()
    for i in range(len(original_matrix)):
        for j in range(len(original_matrix[i])):
            if original_matrix[i][j] != "#":
                old_matrix = np.copy(original_matrix)
                old_matrix[i][j] = "#"
                a, b = move_cursor_game(old_matrix)
                if a is not None and b is not None:
                    print(a, b)
                    new_positions.add((i, j))

    return new_positions


def main():
    input_file = open("input.txt", "r")
    for line in input_file:
        char_arr = []
        char_arr.extend(line.strip())
        original_matrix.append(char_arr)
    a = move_cursor_game_with_new_obstacle()
    # move_cursor_game()
    print("".join(sum(original_matrix, [])).count("X"))

    print(len(a))
    print(a)


main()
