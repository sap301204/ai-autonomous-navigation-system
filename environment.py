import numpy as np


def create_street_grid(rows=40, cols=40):
    """
    Creates a street-like navigation grid.
    0 = free space
    1 = obstacle/wall
    """
    grid = np.ones((rows, cols), dtype=int)

    # Create horizontal roads
    horizontal_roads = [2, 9, 16, 24, 32, 37]
    for r in horizontal_roads:
        grid[r:r+2, :] = 0

    # Create vertical roads
    vertical_roads = [3, 8, 12, 15, 19, 24, 30, 35]
    for c in vertical_roads:
        grid[:, c:c+2] = 0

    # Add some blockages to make it interesting
    grid[9:16, 8:10] = 1
    grid[2:9, 15:17] = 1
    grid[24:32, 24:26] = 1
    grid[16:24, 30:32] = 1
    grid[32:37, 12:14] = 1

    # Re-open a few areas so paths still exist
    grid[12:14, 8:10] = 0
    grid[5:7, 15:17] = 0
    grid[27:29, 24:26] = 0
    grid[19:21, 30:32] = 0
    grid[34:36, 12:14] = 0

    return grid


def get_start_goal(grid):
    """
    Returns valid start and goal points on free cells.
    """
    start = (37, 20)
    goal = (29, 36)

    if grid[start] == 1 or grid[goal] == 1:
        raise ValueError("Start or Goal is placed on an obstacle. Adjust coordinates.")

    return start, goal