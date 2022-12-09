num = int(input())

chess = []
horses = []
for i in range(num):
    row = list(input())
    chess.append(row)
    for j in range(num):
        if chess[i][j] == "K":
            horses.append((i, j))


def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n


def all_moves(r, c, chess, n):
    danger = 0
    if is_valid(r - 2, c - 1, n):
        if chess[r - 2][c - 1] == "K":
            danger += 1
    if is_valid(r - 1, c - 2, n):
        if chess[r - 1][c - 2] == "K":
            danger += 1
    if is_valid(r + 1, c - 2, n):
        if chess[r + 1][c - 2] == "K":
            danger += 1
    if is_valid(r + 2, c - 1, n):
        if chess[r + 2][c - 1] == "K":
            danger += 1
    if is_valid(r + 2, c + 1, n):
        if chess[r + 2][c + 1] == "K":
            danger += 1
    if is_valid(r + 1, c + 2, n):
        if chess[r + 1][c + 2] == "K":
            danger += 1
    if is_valid(r - 1, c + 2, n):
        if chess[r - 1][c + 2] == "K":
            danger += 1
    if is_valid(r - 2, c + 1, n):
        if chess[r - 2][c + 1] == "K":
            danger += 1
    return danger

most_danger, to_remove = 0, 0



knight_r, knight_c = 0, 0
while True:
    for horse in horses:
        danger = 0
        danger = all_moves(horse[0], horse[1], chess, num)
        if danger > most_danger:
            most_danger = danger
            knight_r, knight_c = horse[0], horse[1]
    if most_danger > 0:
        chess[knight_r][knight_c] = "-"
        if (knight_r, knight_c) in horses:
            horses.remove((knight_r, knight_c))
        knight_r, knight_c = 0, 0
        most_danger = 0
        to_remove += 1
    elif danger == 0:
        print(to_remove)
        break
    