from math import ceil

rows, cols = [int(x) for x in input().split()]
text = input()
text = text * ceil(rows * cols / len(text))

# matrix = []
for i in range(rows):
    curr_text = text[:cols]
    text = text[cols:]
    if i % 2 == 0:
        # matrix.append(curr_text)
        print(curr_text)
    else:
        # matrix.append(curr_text[::-1])
        print(curr_text[::-1])
