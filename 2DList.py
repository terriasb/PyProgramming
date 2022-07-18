#  standard list number_grid = [1, 2, 3, 4]

number_grid = [
            [1, 2, 8],   # the first number is [0][0] = 1 [0][1] = 2 [0][2] = 8
            [2, 1, 5],
            [3, 1, 2],
            [0]
]  # list within list or a matrix list

# accessing matrix elements
# print(number_grid[0][2])

for row in number_grid:
    for col in row:
        print(col)