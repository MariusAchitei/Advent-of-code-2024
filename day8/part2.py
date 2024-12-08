from collections import defaultdict

inputs = list()


def group_elements(matrix):
    groued_elements = defaultdict(list)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == ".":
                continue
            if matrix[i][j] in groued_elements:
                groued_elements[matrix[i][j]].append((i, j))
            else:
                groued_elements[matrix[i][j]] = [(i, j)]
    return groued_elements


def calculate_distances(matrix, grouped_elements):

    resonances = set()

    for key, value in grouped_elements.items():
        for i in range(0, len(value) - 1):
            for j in range(i + 1, len(value)):
                x1, y1 = grouped_elements[key][i]
                x2, y2 = grouped_elements[key][j]

                a = x1 + (x1 - x2)
                b = y1 + (y1 - y2)
                d1s = []
                while 0 <= a < len(matrix) and 0 <= b < len(matrix[a]):
                    d1s += [(a, b)]
                    a += (x1 - x2)
                    b += (y1 - y2)

                a = x2 + (x2 - x1)
                b = y2 + (y2 - y1)
                d2s = []
                while 0 <= a < len(matrix) and 0 <= b < len(matrix[a]):
                    d2s += [(a, b)]
                    a += (x2 - x1)
                    b += (y2 - y1)

                resonances = resonances.union(set(d1s))
                resonances = resonances.union(set(d2s))

    return list(resonances)


def filter_resonances(resonances, matrix):

    new_resonances = []

    for resonance in resonances:
        x, y = resonance
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]):
            new_resonances.append(resonance)
    return new_resonances

    # return [resonance for index, resonance in resonances if
    #         0 <= int(resonance[0]) < len(matrix) and 0 <= int(resonance[1]) < len(matrix[index])]


def append_resonances(matrix, filtered_resonances):
    for resonance in filtered_resonances:
        x, y = resonance
        matrix[x][y] = "#"
    return matrix


def add_anntenas_to_resonances(matrix, antennas, filtered_resonances):
    resonances = set(filtered_resonances)
    return resonances.union(set(antennas))


def main():
    sum = 0
    rezults = {}
    matrix = []
    input_file = open("input.txt", "r")
    for line in input_file:
        char_arr = []
        char_arr.extend(line.strip())
        matrix.append(char_arr)

    grouped_elements = dict(group_elements(matrix))

    antennas = []

    for key, value in grouped_elements.items():
        antennas += value

    resonances = calculate_distances(matrix, grouped_elements)

    filtered_resonances = filter_resonances(resonances, matrix)

    matrix = append_resonances(matrix, filtered_resonances)

    all = add_anntenas_to_resonances(matrix, antennas, filtered_resonances)

    [print(line) for line in matrix]

    print(grouped_elements)

    print(resonances)

    print(len(all))

    print(sum)


main()
