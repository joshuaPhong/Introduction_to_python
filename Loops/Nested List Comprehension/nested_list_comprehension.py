string = '0123456789'

matrix = [[j for j in range((string[0:9]))] for i in range((string[0:9]))]

for row in matrix:
    print(row)
