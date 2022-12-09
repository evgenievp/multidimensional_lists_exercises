rows, cols = [int(x) for x in input().split()]
matrix = []

for r in range(rows):
    for c in range(cols):
        current_col = f"{chr(97+r)}{chr(97+c + r)}{chr(97+r)}"
        if current_col == current_col[::-1]:
            print(current_col, end=' ')
    print()
