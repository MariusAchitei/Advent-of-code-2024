import numpy as np

directions = {"^": {"self": "^", "next": ">", "move": lambda i, j: (i - 1, j)},
    ">": {"self": ">", "next": "v", "move": lambda i, j: (i, j + 1)},
    "v": {"self": "v", "next": "<", "move": lambda i, j: (i + 1, j)},
    "<": {"self": "<", "next": "^", "move": lambda i, j: (i, j - 1)}}

matrix = []

# collisions = set()

path = set()


def find_cursor():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in directions:
                return i, j, directions[matrix[i][j]]
    return None, None, None


def is_inside_matrix(i, j):
    if i is None or j is None:
        return False
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def is_obstacle(i, j, direction):
    return matrix[i][j] == "#"


a = set()


def move_cursor(i, j, direction):
    matrix[i][j] = direction["self"]


def move_cursor_game():
    i, j, direction = find_cursor()
    index = 0
    while is_inside_matrix(i, j):
        (i, j, direction) = find_cursor()
        nexti, nextj = direction["move"](i, j)
        if not is_inside_matrix(nexti, nextj):
            matrix[i][j] = index
            index += 1
            path.add((oldi, oldj, direction["self"]))
            break
        if is_obstacle(nexti, nextj, direction):
            direction = directions[direction["next"]]
        else:
            oldi, oldj = i, j
            i, j = direction["move"](i, j)
            matrix[oldi][oldj] = index
            index += 1
            path.add((oldi, oldj, direction["self"]))
        move_cursor(i, j, direction)


def corresponding_top(i, j, top_obstacles):
    if i is None or j is None:
        return None
    on_the_same_column = [obstacle for obstacle in top_obstacles if obstacle[1] == j and obstacle[0] < i]
    if len(on_the_same_column) == 0:
        return None
    return max([obstacle[0] for obstacle in on_the_same_column]) + 1


def corresponding_right(i, j, right_obstacles):
    if i is None or j is None:
        return None
    on_same_line = [obstacle for obstacle in right_obstacles if obstacle[0] == i and obstacle[1] > j]
    if len(on_same_line) == 0:
        return None
    return min([obstacle[1] for obstacle in on_same_line]) - 1


def corresponding_bottom(i, j, bottom_obstacles):
    if i is None or j is None:
        return None
    on_the_same_column = [obstacle for obstacle in bottom_obstacles if obstacle[1] == j and obstacle[0] > i]
    if len(on_the_same_column) == 0:
        return None
    return min([obstacle[0] for obstacle in on_the_same_column]) - 1


def corresponding_left(i, j, left_obstacles):
    if i is None or j is None:
        return None
    on_same_line = [obstacle for obstacle in left_obstacles if obstacle[0] == i and obstacle[1] < j]
    if len(on_same_line) == 0:
        return None
    return max([obstacle[1] for obstacle in on_same_line]) + 1


def extract_obstacles():
    obstacles2 = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "#":
                obstacles2.add((i, j))
    return list(obstacles2)


def process_collisions():
    obstacles = extract_obstacles()

    loops = set()

    for spot in sorted(list(path)):
        i, j = spot[0], spot[1]
        if i == 8 and j == 4:
            print("here")
        direction = spot[2]
        if direction == "^":
            right_column = corresponding_right(i, j, obstacles)
            bottom_line = corresponding_bottom(i, right_column, obstacles)
            left_column = corresponding_right(bottom_line, right_column, obstacles)
            if left_column is not None and left_column == j:
                loops.add((i - 1, j))
        elif direction == "v":
            left_column = corresponding_left(i, j, obstacles)
            top_line = corresponding_top(i, left_column, obstacles)
            right_column = corresponding_right(top_line, left_column, obstacles)
            if right_column is not None and right_column == j:
                loops.add((i + 1, j))

        elif direction == "<":
            top_line = corresponding_top(i, j, obstacles)
            right_column = corresponding_right(top_line, j, obstacles)
            bottom_line = corresponding_bottom(top_line, right_column, obstacles)
            if bottom_line is not None and bottom_line == i:
                loops.add((i, j - 1))
        elif direction == ">":
            bottom_line = corresponding_bottom(i, j, obstacles)
            left_column = corresponding_left(bottom_line, j, obstacles)
            top_line = corresponding_top(bottom_line, left_column, obstacles)
            if top_line is not None and top_line == i:
                loops.add((i, j + 1))
    print(len(loops))
    print(loops)
    for loop in loops:
        matrix[loop[0]][loop[1]] = "O"
    # print_matrix()


def print_matrix():
    new = np.copy(matrix)
    print('\n'.join([f"{j}   " + f'\t'.join([str(cell) for cell in row]) for j, row in enumerate(new)]))


def main():
    input_file = open("input.txt", "r")
    for line in input_file:
        char_arr = []
        char_arr.extend(line.strip())
        matrix.append(char_arr)
    move_cursor_game()
    # print_matrix()
    process_collisions()


main()

# {(7, 7), (8, 1), (8, 3), (7, 6), (6, 3), (9, 7)}

# {(8, 7), (6, 4), (7, 6), (6, 6), (8, 2)}
