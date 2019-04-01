import math
import pprint


def check_duplicates(vector):
    vector = list(filter(lambda x: x != 0, vector))
    return len(vector) == len(set(vector))


# this is a O(n2) function in total; this code is mainly to check how you can write readable Python
def is_valid_sudoku(grid):
    if all(check_duplicates(row) for row in grid) and all(check_duplicates(col) for col in list(zip(*grid))):
        # now check within the mini squares
        region_size = int(math.sqrt(len(grid)))
        for i in range(region_size):
            for j in range(region_size):
                if not check_duplicates([grid[x][y] for x in range(i*region_size, (i+1)*region_size)
                                         for y in range(j*region_size, (j+1)*region_size)]):
                    return False
        return True


# Check whether a 9x9 2D array representing a partial Sudoku is valid or not. Specifically, check that no row, column or
# 3x3 sub-array contains duplicates. A 0-value in the 2D array represents a blank, and 1-9 value represents a number.


grid_ = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

pprint.pprint(grid_)
print(is_valid_sudoku(grid_))


