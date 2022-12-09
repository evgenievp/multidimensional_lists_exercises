n = int(input())

mat = []
for i in range(n):
    row = [int(x) for x in input().split()]
    mat.append(row)


line = input()

while line != "END":
    do = line.split()
    if do[0] == "Add":
        if 0 <= int(do[1]) < n and 0 <= int(do[2]) < n:
            mat[int(do[1])][int(do[2])] += int(do[3])
        else:
            print("Invalid coordinates")

    elif do[0] == "Subtract":
        if 0 <= int(do[1]) < n and 0 <= int(do[2]) < n:
            mat[int(do[1])][int(do[2])] -= int(do[3])
        else:
            print("Invalid coordinates")
    else:
        print("Invalid coordinates")

    line = input()

for i in range(n):
    print(*mat[i])
