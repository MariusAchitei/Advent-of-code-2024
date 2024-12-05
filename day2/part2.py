def main():
    matrix = list()
    input_file = open("input.txt", "r")
    for line in input_file:
        parts = line.split(" ")
        parts = [int(elem) for elem in parts]
        matrix.append(parts)


    safe = 0
    for line in matrix:
        if check_line_skip1(line):
            safe+=1

    print(safe)


def check_line_skip1(line):
    if check_line(line):
        return True
    for i in range(len(line)):
        if check_line(line[:i] + line[i + 1:]):
            return True
    return False


def check_line(line):
    sgn = (line[0] - line[1]) > 0
    for i in range(1, len(line)):
        difference = line[i - 1] - line[i]
        if abs(difference) > 3 or abs(difference) < 1:
            return False
        if (difference > 0) != sgn:
            return False
    return True

main()