def find(matrix: [[], ], number: int) -> bool:
    row = 0
    column = len(matrix[0]) - 1

    while column >= 0 and row < len(matrix):
        print(f"{row}-{column}")
        if matrix[row][column] == number:
            return True
        elif matrix[row][column] > number:
            column -= 1
        elif matrix[row][column] < number:
            row += 1

    return False


if __name__ == '__main__':
    test_matrix = [[4, 9, 12], [7, 10, 13], [8, 11, 15]]
    print(find(test_matrix, 100))

