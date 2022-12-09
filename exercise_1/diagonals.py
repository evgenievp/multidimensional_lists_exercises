n = int(input())
board = []
for i in range(n):
    board.append([int(x) for x in input().split(", ")])


reverse = n - 1
left, right = 0, 0
left_nums, right_nums = [], []
for i in range(n):
    left += board[i][i]
    left_nums.append(str(board[i][i]))


for i in range(n):
    right += board[i][reverse]
    right_nums.append(str(board[i][reverse]))
    reverse -= 1

print(f"Primary diagonal: {', '.join(left_nums)}. Sum: {left}")
print(f"Secondary diagonal: {', '.join(right_nums)}. Sum: {right}")
