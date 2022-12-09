def valid(direction, steps, row, col, board):
    if direction == "up":
        if (row - steps) >= 0:
            if board[row - steps][col] == ".":
                return True
    elif direction == "down":
        if (row + steps) < 5:
            if board[row + steps][col] == ".":
                return True
    elif direction == "left":
        if (col - steps) >= 0:
            if board[row][col - steps] == ".":
                return True
    elif direction == "right":
        if (col + steps) < 5:
            if board[row][col + steps] == ".":
                return True
    return False


def new_pos(steps, row, col, board, direction):
    if direction == "up":
        board[row - steps][col] = "A"
        return (row - steps), col, board
    elif direction == "down":
        board[row + steps][col] = "A"
        return (row + steps), col, board
    elif direction == "left":
        board[row][col - steps] = "A"
        return row, (col - steps), board
    elif direction == "right":
        board[row][col + steps] = "A"
        return row, (col + steps), board
    return row, col, board


def shoot(row, col, board, target, direction):
    if direction == "up":
        for i in range(row, -1, -1):
            if board[i][col] == "x":
                target.append((i, col))
                board[i][col] = "."
                return target, board
    elif direction == "down":
        for i in range(row, 5):
            if board[i][col] == "x":
                target.append((i, col))
                board[i][col] = '.'
                return target, board
    elif direction == "left":
        for i in range(col, -1, -1):
            if board[row][i] == "x":
                target.append((row, i))
                board[row][i] = '.'
                return target, board
    elif direction == "right":
        for i in range(col, 5):
            if board[row][i] == "x":
                target.append((row, i))
                board[row][i] = '.'
                return target, board
    return target, board


my_row, my_col, targets_count = 0, 0, 0
field = []
targets = []
for a in range(5):
    cur_row = input().split()
    field.append(cur_row)
    for b in range(5):
        if field[a][b] == "A":
            my_row, my_col = a, b
        if field[a][b] == "x":
            targets_count += 1

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "shoot":
        targets, field = shoot(my_row, my_col, field, targets, command[1])
    elif command[0] == "move":
        step = int(command[2])
        if valid(command[1], step, my_row, my_col, field):
            field[my_row][my_col] = "."
            my_row, my_col, field = new_pos(step, my_row, my_col, field, command[1])
            field[my_row][my_col] = "A"

if len(targets) < targets_count:
    count_left_targets = targets_count - len(targets)
    print(f"Training not completed! {count_left_targets} targets left.")
else:
    print(f"Training completed! All {len(targets)} targets hit.")
for k, v in targets:
    print(f"[{k}, {v}]")