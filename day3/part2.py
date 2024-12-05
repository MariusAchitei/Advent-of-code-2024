def main():
    matrix = list()
    input_file = open("input.txt", "r")
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
    fail = 0
    sgn = (line[0] - line[1]) > 0
    for i in range(1, len(line)):
        if abs(line[i - 1] - line[i]) > 3 or abs(line[i - 1] - line[i]) < 1:
            fail += 1
        elif (line[i - 1] - line[i] > 0) != sgn:
            fail += 1
    if fail < 2:
        return True
    else:
        return False


main()