def contains_word(string):
    return "MAS" in string or "SAM" in string

def contains_x_mas(lens):
    main_diag = "".join([lens[0][0], lens[1][1], lens[2][2]])
    second_diag = "".join([lens[0][2], lens[1][1], lens[2][0]])
    return contains_word(main_diag) and contains_word(second_diag)


def search_x_mas(matrix):
    count = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            lens = [matrix[i-1][j-1:j+2], matrix[i][j-1:j+2], matrix[i+1][j-1:j+2]]
            if contains_x_mas(lens):
                count+=1
    return count


def main():
    matrix = []
    input_file = open("input.txt", "r")
    for line in input_file:
        char_arr = []
        char_arr.extend(line.strip())
        matrix.append(char_arr)

    a = search_x_mas(matrix)

    print(a)

main()