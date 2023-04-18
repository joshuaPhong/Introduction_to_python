string = '0123456789'

matrix = [[i for i in string] for j in range(10)]

for row in matrix:
    print(row)
matrix2 = []
for i in range(len(string)):
    matrix2.append([])
    for j in range(0, 10, 2):
        var = matrix2[i].append(j)
        print(matrix2)

