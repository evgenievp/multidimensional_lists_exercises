n = int(input())
board = []
for i in range(n):
    board.append([int(x) for x in input().split(" ")])


reverse = n - 1
left, right = 0, 0
for i in range(n):
    left += board[i][i]


for i in range(n):
    right += board[i][reverse]
    reverse -= 1

print(abs(left - right))
