def new_position(santa_r, santa_c, direction):
    if direction == "up":
        return santa_r - 1, santa_c
    elif direction == "down":
        return santa_r + 1, santa_c
    elif direction == "left":
        return santa_r, santa_c - 1
    return santa_r, santa_c + 1


presents_count = int(input())
n = int(input())
neighboard = []
santa_row, santa_col, nice_kids, kids = 0, 0, 0, 0
for r in range(n):
    row = input().split()
    neighboard.append(row)
    for c in range(n):
        if neighboard[r][c] == "S":
            santa_row, santa_col = r, c
        if neighboard[r][c] == "V":
            nice_kids += 1
            kids += 1
count_nice_kids = nice_kids

while presents_count:
    command = input()
    if command == "Christmas morning":
        break
    neighboard[santa_row][santa_col] = "-"
    santa_row, santa_col = new_position(santa_row, santa_col, command)
    if neighboard[santa_row][santa_col] == "X":
        neighboard[santa_row][santa_col] = "-"
    elif neighboard[santa_row][santa_col] == "V":
        neighboard[santa_row][santa_col] = "-"
        if presents_count > 0:
            presents_count -= 1
            nice_kids -= 1
        else:
            break
    elif neighboard[santa_row][santa_col] == "C":
        if neighboard[santa_row][santa_col - 1] in "VX":
            if presents_count > 0:
                presents_count -= 1
            else:
                break
            if neighboard[santa_row][santa_col - 1] == "V":
                nice_kids -= 1
            neighboard[santa_row][santa_col -1] = "-"
        if neighboard[santa_row][santa_col + 1] in "VX":
            if presents_count > 0:
                presents_count -= 1
            else:
                break
            if neighboard[santa_row][santa_col + 1] == "V":
                nice_kids -= 1
            neighboard[santa_row][santa_col + 1] = "-"
        if neighboard[santa_row - 1][santa_col] in "VX":
            if presents_count > 0:
                presents_count -= 1
            else:
                break
            if neighboard[santa_row - 1][santa_col] == "V":
                nice_kids -= 1
            neighboard[santa_row - 1][santa_col] = "-"
        if neighboard[santa_row + 1][santa_col] in "VX":
            if presents_count > 0:
                presents_count -= 1
            else:
                break
            if neighboard[santa_row + 1][santa_col] == "V":
                nice_kids -= 1
            neighboard[santa_row + 1][santa_col] = "-"
    neighboard[santa_row][santa_col] = "S"

if presents_count < 1 and nice_kids > 0:
    print("Santa ran out of presents!")

for _ in range(n):
    print(*neighboard[_])

if nice_kids < 1:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
