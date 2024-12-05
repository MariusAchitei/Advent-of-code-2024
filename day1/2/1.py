from itertools import count


def main():
    left = list()
    right = list()
    input_file = open("input.txt", "r")
    for line in input_file:
        line = line.replace("   ", " ")
        parts = line.split(" ")
        left.append(int(parts[0]))
        right.append(int(parts[1]))

    left = list(sorted(left))
    right = list(sorted(right))

    distance = 0

    for num in left:
        distance += right.count(num) * num

    print(distance)

main()