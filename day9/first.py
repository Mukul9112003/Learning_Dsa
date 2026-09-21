nums = [[5, 8, 9], [10, 7, 6], [3, 1, 2]]
nums1 = [[5, 8, 9, 10], [10, 7, 6, 8], [3, 1, 2, 7]]


def set_zeroes(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rowtrack = [0 for _ in range(rows)]
    columnstrack = [0 for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                rowtrack[i] = -1
                columnstrack[j] = -1
    for i in range(rows):
        for j in range(columns):
            if rowtrack[i] == -1 or columnstrack[j] == -1:
                matrix[i][j] = 0


def display(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end=" ")
        print()


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result = [[0] * rows for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            result[j][i] = matrix[i][j]
    return result


set_zeroes(nums)
display(nums)
print("Transpose")
result = transpose(nums1)
display(result)
