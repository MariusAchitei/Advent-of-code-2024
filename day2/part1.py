def main():
    matrix = list()
    input_file = open("1/input.txt", "r")
    for line in input_file:
        parts = line.split(" ")
        parts = [int(elem) for elem in parts]
        matrix.append(parts)


    safe = 0
    for line in matrix:
        if  len(line) <= 3:
            print (line)
        if check_line(line):
            # print(line)
            safe+=1

    print(safe)


def check_line(line):
    sgn = (line[0] - line[1]) > 0
    for i in range(1, len(line)):
        if abs(line[i - 1] - line[i]) > 3 or abs(line[i - 1] - line[i]) < 1:
            return  False
        if (line[i - 1] - line[i] > 0) != sgn:
            return False

    return True


main()