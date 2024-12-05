def main():
    matrix = read_matrix("input.txt")
    safe = count_safe_lines(matrix, check_line)
    print(safe)

def read_matrix(file_path):
    with open(file_path, "r") as input_file:
        return [list(map(int, line.split())) for line in input_file]

def count_safe_lines(matrix, check_function):
    return sum(1 for line in matrix if check_function(line))


def check_line(line):
    sgn = (line[0] - line[1]) > 0
    for i in range(1, len(line)):
        difference = line[i - 1] - line[i]
        if abs(difference) > 3 or abs(difference) < 1:
            return  False
        if (difference > 0) != sgn:
            return False

    return True


main()