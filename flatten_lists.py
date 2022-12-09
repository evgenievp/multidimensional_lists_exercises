sublists = input().split("|")
result = []

for idx in range(len(sublists) - 1, -1, -1):
    elements = sublists[idx].split()
    result += elements

print(*result, sep=' ')