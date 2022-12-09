rows, cols = [int(x) for x in input().split()]
m = []
for _ in range(rows):
    m.append([int(x) for x in input().split()])

max_sum = 0
for r in range(rows - 2):
    for c in range(cols - 2):
        cur_matrix = [m[r][c], m[r][c + 1], m[r][c + 2], \
                      m[r + 1][c], m[r + 1][c + 1], m[r + 1][c + 2], \
                      m[r + 2][c], m[r + 2][c + 1], m[r + 2][c + 2]]
        if sum(cur_matrix) >= max_sum:
            max_sum = sum(cur_matrix)
            best_matrix = r, c

print(f"Sum = {max_sum}")
r = int(best_matrix[0])
c = int(best_matrix[1])

print(' '.join(str(x) for x in m[r][c:c + 3]))
print(' '.join(str(x) for x in m[r + 1][c: c + 3]))
print(' '.join(str(x) for x in m[r + 2][c: c + 3]))
