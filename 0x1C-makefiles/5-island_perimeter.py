#!/usr/bin/python3
""" File defining perimeter of a island """


def island_perimeter(grid):
    """
    Function to return the perimeter of island.
    No Island : Perimeter is 0 if not 1 found in array.
        Each time it has land near, reduces perimeter value by 1,
        Or if there is water, increase perimeter value by 1.
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return (perimeter)
