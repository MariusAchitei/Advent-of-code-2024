directions = {
    "^": {"self": "^","next":">","move": lambda i, j: (i-1, j)},
    ">": {"self": ">","next":"v","move": lambda i, j: (i, j+1)},
    "v": {"self": "v","next":"<","move": lambda i, j: (i+1, j)},
    "<": {"self": "<","next":"^","move": lambda i, j: (i, j-1)}
}

matrix = []

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
    i, j, direction =  find_cursor()
    while is_inside_matrix(i, j):
        (i, j, direction) = find_cursor()
        nexti, nextj = direction["move"](i, j)
        if not is_inside_matrix(nexti, nextj):
            matrix[i][j] = "X"
            break
        if is_obstacle(nexti, nextj, direction):
            direction = directions[direction["next"]]
        else:
            oldi, oldj = i, j
            i, j = direction["move"](i, j)
            matrix[oldi][oldj] = "X"
        move_cursor(i, j, direction)
def main():
    input_file = open("input.txt", "r")
    for line in input_file:
        char_arr = []
        char_arr.extend(line.strip())
        matrix.append(char_arr)
    move_cursor_game()
    print("".join(sum(matrix, [])).count("X"))


main()