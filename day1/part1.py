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

    distance = sum([abs(l - r) for (l, r) in zip(left, right)])



    print(distance)

main()