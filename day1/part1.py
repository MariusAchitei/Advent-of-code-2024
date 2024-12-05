def main():
    left = list()
    right = list()
    input_file = open("1/input.txt", "r")
    for line in input_file:
        line = line.replace("   ", " ")
        parts = line.split(" ")
        left.append(parts[0])
        right.append(parts[1])

    left = list(sorted(left))
    right = list(sorted(right))

    distance = 0
    for i in range(len(left)):
        distance += abs(int(left[i]) - int(right[i]))

    print(distance)
    # a = search_x_mas(matrix)

    # print(a)

main()