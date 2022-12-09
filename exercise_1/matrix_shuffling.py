rows, cols = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    row = [x for x in input().split()]
    matrix.append(row)

line = input()
while line != "END":
    do = line.split()
    if do[0] == "swap":
        if len(do) == 5:
            row_1, col_1, row_2, col_2 = [int(x) for x in do[1:]]
            if 0 <= row_1 < rows and 0 <= col_1 < cols and 0 <= row_2 < rows and 0 <= col_2 < cols:
                sym = matrix[row_1][col_1]
                matrix[row_1][col_1] = matrix[row_2][col_2]
                matrix[row_2][col_2] = sym
                for i in range(rows):
                    print(*matrix[i])
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    line = input()

